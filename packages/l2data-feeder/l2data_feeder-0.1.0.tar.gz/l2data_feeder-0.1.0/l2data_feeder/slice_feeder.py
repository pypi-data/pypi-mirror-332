
import os
import time
import datetime
import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, List, Dict, Generator, Union

# 从 l2data_reader pip模块中导入 MarketDataReader 以及消息中涉及的对象
from l2data_reader import (
    MarketDataHeader, MarketDataReader,
    TransactionEntrustData,
    SecuDepthMarketData, TransactionTradeData,
    Direction, TrdType,
    DIRECTION_MAP, TRD_TYPE_MAP
)

# 定义用于策略引擎的 Snapshot 与 Slice 数据结构
@dataclass
class Snapshot:
    Symbol: str
    Tick: Optional[SecuDepthMarketData]    # 此处类型用 object 表示，实际代码中可替换为 SecuDepthMarketData 类型
    Orders: List[TransactionEntrustData]      # 实际可替换为 TransactionEntrustData 类型
    Transactions: List[TransactionTradeData]  # 实际可替换为 TransactionTradeData 类型

@dataclass
class Slice:
    Ticks: Dict[str, Snapshot]


class Level2SliceFeeder:
    def __init__(
        self,
        logger: logging.Logger,
        index_file: str,
        data_file: str,
        header_file: Optional[str] = None,
        slice_interval_ms: int = 5000,
        prefetch_count: int = 0,
        realtime: bool = False
    ):
        """
        初始化 Level2SliceFeeder 对象

        参数:
          logger: 日志记录器对象
          index_file: Level2 数据索引文件路径
          data_file: Level2 数据文件路径
          header_file: Level2 数据头文件路径（可选）
          slice_interval_ms: 每个时间片的间隔（毫秒）
          prefetch_count: 数据预取的消息数，0 表示不预取，-1 表示读取全部，正数表示读取指定条数
          realtime: 是否启用实时更新模式（预取完成后继续读取新数据，并 yield 返回 Slice 对象）
        """
        self.logger = logger
        self.index_file = index_file
        self.data_file = data_file
        self.header_file = header_file
        self.slice_interval_ms = slice_interval_ms
        self.prefetch_count = prefetch_count
        self.realtime = realtime
        
        # 初始化 MarketDataReader（若提供 header_file，则使用四个参数初始化，否则使用三个参数）
        if self.header_file:
            self.reader = MarketDataReader(self.logger, self.index_file, self.data_file, self.header_file)
        else:
            self.reader = MarketDataReader(self.logger, self.index_file, self.data_file)
            
        # 使用一个字典保存当前时间片内每个 symbol 的聚合数据
        # key: symbol; value: Snapshot 对象
        self.current_slice: Dict[str, Snapshot] = {}
        # 当前时间片起始时间（毫秒），使用系统时间
        self.slice_start_time: Optional[int] = None
        # 标识 feeder 是否应持续运行（主要用于实时模式）
        self.running = True

    def _process_message(self, header, market_data) -> None:
        """
        根据消息类型(1001: tick, 1002: 委托, 1003: 成交)处理消息，
        将不同消息按 symbol 聚合到 current_slice 中。

        使用当前系统时间（毫秒）作为时间片起始参考
        """
        current_time = int(time.time() * 1000)
        if self.slice_start_time is None:
            self.slice_start_time = current_time

        # 根据消息类型进行处理
        if header.msg_type == 1001:
            # Tick 数据处理（行情数据）
            tick = market_data.secu_depth_market_data
            symbol = tick.symbol
            if symbol not in self.current_slice:
                self.current_slice[symbol] = Snapshot(Symbol=symbol, Tick=None, Orders=[], Transactions=[])
            self.current_slice[symbol].Tick = tick
        elif header.msg_type == 1002:
            # 订单数据处理（逐笔委托数据）
            order = market_data.transaction_entrust_data
            symbol = order.symbol
            if symbol not in self.current_slice:
                self.current_slice[symbol] = Snapshot(Symbol=symbol, Tick=None, Orders=[], Transactions=[])
            self.current_slice[symbol].Orders.append(order)
        elif header.msg_type == 1003:
            # 成交数据处理（逐笔成交数据）
            trade = market_data.transaction_trade_data
            symbol = trade.symbol
            if symbol not in self.current_slice:
                self.current_slice[symbol] = Snapshot(Symbol=symbol, Tick=None, Orders=[], Transactions=[])
            self.current_slice[symbol].Transactions.append(trade)
        else:
            # 其他类型消息可根据需要增加处理逻辑
            pass

    def _push_slice(self, current_time: int) -> Slice:
        """
        将当前聚合的消息打包为一个 Slice 对象，
        并清空当前的聚合数据，同时更新 slice 起始时间

        参数:
          current_time: 当前系统时间（毫秒），用于刷新时间片起始时间
        返回:
          一个包含当前 Slice 数据的 Slice 对象
        """
        new_slice = Slice(Ticks=dict(self.current_slice))
        self.current_slice.clear()
        self.slice_start_time = current_time
        self.logger.debug(f"生成新 Slice 对象，更新时间片起始时间为 {current_time} 毫秒")
        return new_slice

    def _prefetch(self) -> List[Slice]:
        """
        执行数据预取操作，从数据文件中读取指定数量的消息
        返回值:
          包含若干 Slice 对象的列表
        """
        slices: List[Slice] = []
        processed_count = 0

        while True:
            res = self.reader.read_next()
            if res is None:
                # 数据结束
                self.logger.info("预取模式下，已无更多数据")
                break

            header, market_data = res
            processed_count += 1
            self._process_message(header, market_data)
            now = int(time.time() * 1000)
            if now - self.slice_start_time >= self.slice_interval_ms:
                s = self._push_slice(now)
                slices.append(s)

            # 若指定了预取消息数量（不为 -1），达到数量后退出
            if self.prefetch_count != -1 and processed_count >= self.prefetch_count:
                self.logger.info(f"预取模式下，已读取 {processed_count} 条消息，达到设定上限")
                break

        # 推送最后剩余的数据（如果存在）
        if self.current_slice:
            now = int(time.time() * 1000)
            s = self._push_slice(now)
            slices.append(s)

        return slices

    def _realtime(self) -> Generator[Slice, None, None]:
        """
        实时数据更新生成器。不断读取数据，
        若当前没有新数据则等待；当收集的数据累积超过时间间隔时 yield 返回一个新的 Slice 对象。
        """
        self.logger.info("启动实时更新模式")
        while self.running:
            res = self.reader.read_next()
            if res is None:
                now = int(time.time() * 1000)
                # 如果当前聚合数据非空且达到时间间隔，则推送当前 Slice
                if self.slice_start_time is not None and self.current_slice and (now - self.slice_start_time >= self.slice_interval_ms):
                    yield self._push_slice(now)
                time.sleep(0.1)
                continue

            header, market_data = res
            self._process_message(header, market_data)
            now = int(time.time() * 1000)
            if now - self.slice_start_time >= self.slice_interval_ms:
                yield self._push_slice(now)

    def run(self) -> Union[List[Slice], Generator[Slice, None, None]]:
        """
        开始数据读取

        工作流程：
         1. 如果 prefetch_count 不为 0，则先执行数据预取，将读取的消息根据 slice_interval_ms 划分成多个 Slice 对象。
         2. 如果实时模式 (realtime=True) 被启用，则在预取完成后继续保持运行，
            不断等待新的数据，并通过 yield 返回新的 Slice 对象；否则直接返回预取的 Slice 列表。

        返回值:
         - 若不启用实时更新，则返回 Slice 对象列表；
         - 启用实时更新，则通过 yield 返回 Slice 对象。
        """
        prefetch_slices: List[Slice] = []
        if self.prefetch_count != 0:
            prefetch_slices = self._prefetch()

        if not self.realtime:
            self.logger.info("预取模式完成，不启用实时更新")
            return prefetch_slices
        else:
            # 若启用实时更新模式，先 yield 出预取结果，再进入实时生成器
            for s in prefetch_slices:
                yield s
            for s in self._realtime():
                yield s

    def stop(self) -> None:
        """
        停止 feeder 的运行
        """
        self.running = False
        if self.reader:
            self.reader.close()
        self.logger.info("Level2SliceFeeder 已停止")