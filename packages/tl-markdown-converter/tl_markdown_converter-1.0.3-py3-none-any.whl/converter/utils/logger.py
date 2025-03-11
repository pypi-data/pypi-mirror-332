"""
日志模块

这个模块负责配置和管理应用程序日志。
"""

import logging
import sys
from pathlib import Path
from typing import Optional

# 导入配置模块
from converter.utils.config import config

# 尝试导入rich模块，用于美化控制台输出
try:
    from rich.logging import RichHandler
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

def setup_logger(name: str, log_file: Optional[str] = None, level: Optional[str] = None) -> logging.Logger:
    """
    配置并返回一个日志记录器
    
    参数:
        name: 日志记录器名称
        log_file: 日志文件路径，如果为None则使用配置中的默认值
        level: 日志级别，如果为None则使用配置中的默认值
    
    返回:
        配置好的日志记录器
    """
    # 获取日志配置
    log_level = level or config.get("logging.level", "INFO")
    log_format = config.get("logging.format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_file = log_file or config.get("logging.file")
    
    # 将字符串日志级别转换为常量
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)
    
    # 清除现有处理器
    logger.handlers = []
    
    # 添加控制台处理器
    if RICH_AVAILABLE:
        # 使用Rich美化控制台输出
        console_handler = RichHandler(rich_tracebacks=True)
        console_handler.setLevel(numeric_level)
        logger.addHandler(console_handler)
    else:
        # 使用标准控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(numeric_level)
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # 如果指定了日志文件，添加文件处理器
    if log_file:
        # 确保日志目录存在
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(numeric_level)
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# 创建默认日志记录器
logger = setup_logger("converter") 