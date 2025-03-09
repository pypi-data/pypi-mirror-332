"""
l2data_feeder - 一个用于实时 Level2 行情数据处理的高效 Python 库

该库能够从 Level2 行情数据文件中读取 tick、订单和成交数据，
并按照指定的时间间隔将这些数据聚合到 Slice 对象中，便于后续分析和处理。
"""

import logging
from typing import Optional

# 导出主要的类和数据结构
from .slice_feeder import (
    Level2SliceFeeder,
    Slice,
    Snapshot
)

# 版本信息
# 动态获取版本信息
try:
    from importlib.metadata import version
    __version__ = version("l2data-feeder")
except ImportError:
    __version__ = "unknown"

def create_default_logger(name: str = "l2data_feeder", level: int = logging.INFO) -> logging.Logger:
    """
    创建默认的日志记录器
    
    参数:
        name: 日志记录器名称
        level: 日志级别
        
    返回:
        配置好的日志记录器
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

def create_feeder(
    index_file: str,
    data_file: str,
    header_file: Optional[str] = None,
    slice_interval_ms: int = 5000,
    prefetch_count: int = 0,
    realtime: bool = False,
    logger: Optional[logging.Logger] = None
) -> Level2SliceFeeder:
    """
    创建 Level2SliceFeeder 实例的便捷函数
    
    参数:
        index_file: Level2 数据索引文件路径
        data_file: Level2 数据文件路径
        header_file: Level2 数据头文件路径（可选）
        slice_interval_ms: 每个时间片的间隔（毫秒）
        prefetch_count: 数据预取的消息数
        realtime: 是否启用实时更新模式
        logger: 日志记录器（如果为 None，则创建默认日志记录器）
        
    返回:
        配置好的 Level2SliceFeeder 实例
    """
    if logger is None:
        logger = create_default_logger()
        
    return Level2SliceFeeder(
        logger=logger,
        index_file=index_file,
        data_file=data_file,
        header_file=header_file,
        slice_interval_ms=slice_interval_ms,
        prefetch_count=prefetch_count,
        realtime=realtime
    )