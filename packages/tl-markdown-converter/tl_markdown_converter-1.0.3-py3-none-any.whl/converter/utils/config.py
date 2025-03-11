"""
配置管理模块

这个模块负责加载和管理应用程序配置。
配置可以从环境变量、配置文件或默认值中获取。
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
import logging

# 尝试导入dotenv，如果安装了的话
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# 默认配置
DEFAULT_CONFIG = {
    # 路径配置
    "paths": {
        "templates_dir": "templates",
        "output_dir": "output",
        "html_dir": "HTML",
        "pdf_dir": "PDF",
        "image_dir": "HTML_to_Image",
    },
    
    # Markdown转HTML配置
    "markdown": {
        "extensions": [
            "markdown.extensions.tables",
            "markdown.extensions.fenced_code",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc",
            "markdown.extensions.nl2br",
            "markdown.extensions.extra"
        ],
        "default_template": "default"
    },
    
    # HTML转PDF配置
    "pdf": {
        "default_format": "both",  # both, print, continuous
        "default_page_format": "A4",
        "default_method": "browser",  # browser, weasyprint
        "margins": {
            "top": "0.4in",
            "right": "0.4in",
            "bottom": "0.4in",
            "left": "0.4in"
        }
    },
    
    # HTML转图片配置
    "image": {
        "width": 720,
        "max_height": 4000,
        "device_scale": 2.0
    },
    
    # 日志配置
    "logging": {
        "level": "DEBUG",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file": "format_converter.log"
    }
}

class Config:
    """配置管理类"""
    
    def __init__(self):
        self._config = DEFAULT_CONFIG.copy()
        self._load_config()
    
    def _load_config(self):
        """加载配置文件"""
        # 尝试从多个位置加载配置文件
        config_paths = [
            Path("config.json"),  # 当前目录
            Path.home() / ".format_converter" / "config.json",  # 用户主目录
            Path(__file__).parent.parent / "config.json"  # 包目录
        ]
        
        for config_path in config_paths:
            if config_path.exists():
                try:
                    with open(config_path, "r", encoding="utf-8") as f:
                        user_config = json.load(f)
                        self._update_config(self._config, user_config)
                    logging.info(f"已加载配置文件: {config_path}")
                    break
                except Exception as e:
                    logging.warning(f"加载配置文件 {config_path} 失败: {e}")
    
    def _update_config(self, target: Dict, source: Dict):
        """递归更新配置字典"""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._update_config(target[key], value)
            else:
                target[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        # 支持点号分隔的键，如 "pdf.default_format"
        if "." in key:
            parts = key.split(".")
            current = self._config
            for part in parts:
                if part not in current:
                    return default
                current = current[part]
            return current
        
        return self._config.get(key, default)
    
    def get_path(self, key: str, default: Optional[str] = None) -> Path:
        """
        获取路径配置，并确保目录存在
        
        参数:
            key: 路径配置键
            default: 默认路径，如果配置中不存在该键
            
        返回:
            Path对象
        """
        path_str = self.get(f"paths.{key}")
        if not path_str and default:
            path_str = default
        elif not path_str:
            return Path(key)
        
        path = Path(path_str)
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    def __getitem__(self, key: str) -> Any:
        """通过字典语法访问配置"""
        return self.get(key)
    
    @property
    def as_dict(self) -> Dict[str, Any]:
        """返回完整配置字典的副本"""
        return self._config.copy()

# 创建全局配置实例
config = Config() 