"""
模板管理模块

这个模块提供了一个模板管理器，用于加载和管理不同的HTML模板。
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

def get_default_templates_dir() -> Path:
    """
    获取默认模板目录路径
    
    返回:
        默认模板目录的Path对象
    """
    # 首先尝试从site-packages获取模板目录
    for path in sys.path:
        if 'site-packages' in str(path):
            site_templates = Path(path) / 'converter' / 'templates'
            print(f"检查site-packages模板目录: {site_templates}")
            if site_templates.exists():
                print(f"site-packages模板目录存在")
                templates = list(site_templates.glob("*/template.html"))
                print(f"找到的模板文件: {templates}")
                if templates:
                    return site_templates
    
    # 如果在site-packages中没有找到，尝试从包内获取
    package_templates = Path(__file__).parent
    print(f"包内模板目录: {package_templates}")
    if package_templates.exists():
        print(f"包内模板目录存在")
        templates = list(package_templates.glob("*/template.html"))
        print(f"找到的模板文件: {templates}")
        if templates:
            return package_templates
    
    # 如果包内没有模板，尝试从当前工作目录查找
    cwd_templates = Path.cwd() / "templates"
    print(f"当前工作目录模板目录: {cwd_templates}")
    if cwd_templates.exists():
        print(f"当前工作目录模板目录存在")
        templates = list(cwd_templates.glob("*/template.html"))
        print(f"找到的模板文件: {templates}")
        if templates:
            return cwd_templates
    
    # 如果都没有找到，返回site-packages目录（如果存在）
    for path in sys.path:
        if 'site-packages' in str(path):
            site_templates = Path(path) / 'converter' / 'templates'
            if site_templates.exists():
                print(f"未找到任何模板，返回site-packages模板目录: {site_templates}")
                return site_templates
    
    # 如果site-packages目录不存在，返回包内模板目录
    print(f"未找到任何模板，返回包内模板目录: {package_templates}")
    return package_templates


class Template:
    """模板类，表示单个模板"""
    
    def __init__(self, template_dir: Path):
        """
        初始化模板
        
        参数:
            template_dir: 模板目录
        """
        self.template_dir = template_dir
        self.name = template_dir.name
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """
        加载模板配置
        
        返回:
            模板配置
        """
        config_path = self.template_dir / "config.json"
        if config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"无法加载模板配置: {str(e)}")
        
        # 返回默认配置
        return {
            "name": self.name.capitalize(),
            "description": "HTML模板",
            "version": "1.0.0",
            "author": "未知",
            "html_template": "template.html",
            "css_files": ["style.css"],
            "js_files": []
        }
    
    def get_html_template(self) -> Path:
        """
        获取HTML模板文件路径
        
        返回:
            HTML模板文件路径
        """
        template_file = self._config.get("html_template", "template.html")
        return self.template_dir / template_file
    
    def get_css_files(self) -> List[Path]:
        """
        获取CSS文件路径列表
        
        返回:
            CSS文件路径列表
        """
        css_files = self._config.get("css_files", ["style.css"])
        return [self.template_dir / css_file for css_file in css_files if (self.template_dir / css_file).exists()]
    
    def get_js_files(self) -> List[Path]:
        """
        获取JavaScript文件路径列表
        
        返回:
            JavaScript文件路径列表
        """
        js_files = self._config.get("js_files", [])
        return [self.template_dir / js_file for js_file in js_files if (self.template_dir / js_file).exists()]
    
    def get_info(self) -> Dict[str, str]:
        """
        获取模板信息
        
        返回:
            模板信息字典
        """
        return {
            "name": self._config.get("name", self.name.capitalize()),
            "description": self._config.get("description", "HTML模板"),
            "version": self._config.get("version", "1.0.0"),
            "author": self._config.get("author", "未知"),
            "preview": self._has_preview()
        }
    
    def _has_preview(self) -> str:
        """
        检查是否有预览图
        
        返回:
            预览图相对路径，如果没有则返回空字符串
        """
        preview_path = self.template_dir / "preview.png"
        if preview_path.exists():
            return str(self.name) + "/preview.png"
        return ""


class TemplateManager:
    """模板管理器类，管理所有可用的模板"""
    
    def __init__(self, templates_dir: Optional[Path] = None):
        """
        初始化模板管理器
        
        参数:
            templates_dir: 模板目录路径
        """
        self.templates_dir = templates_dir or get_default_templates_dir()
        self.templates: Dict[str, Template] = {}
        self._discover_templates()
    
    def _discover_templates(self):
        """发现并加载所有可用的模板"""
        # 确保目录存在
        print(f"正在搜索模板目录: {self.templates_dir}")
        if not self.templates_dir.exists():
            print(f"模板目录不存在: {self.templates_dir}")
            return
        
        print(f"模板目录存在，开始遍历子目录")
        # 遍历目录中的子目录
        for item in self.templates_dir.iterdir():
            print(f"检查目录项: {item}")
            if item.is_dir() and not item.name.startswith('__'):  # 忽略__pycache__等目录
                print(f"发现子目录: {item.name}")
                # 检查是否是有效的模板目录
                template_html = item / "template.html"
                print(f"检查模板文件: {template_html}")
                if template_html.exists():
                    print(f"找到模板文件: {template_html}")
                    try:
                        template = Template(item)
                        self.templates[item.name] = template
                        print(f"成功加载模板: {item.name}")
                    except Exception as e:
                        print(f"加载模板 {item.name} 时出错: {str(e)}")
                else:
                    print(f"模板文件不存在: {template_html}")
        
        print(f"模板搜索完成，找到 {len(self.templates)} 个模板")
    
    def load_template(self, template_name: str) -> Template:
        """
        加载指定名称的模板
        
        参数:
            template_name: 模板名称
        
        返回:
            模板对象
        
        异常:
            ValueError: 如果模板不存在
        """
        if template_name in self.templates:
            return self.templates[template_name]
        
        # 如果没有找到，尝试刷新模板列表
        self._discover_templates()
        
        if template_name in self.templates:
            return self.templates[template_name]
        
        # 如果指定的模板不存在，但default模板存在，则返回default
        if "default" in self.templates and template_name != "default":
            print(f"模板 '{template_name}' 不存在，使用默认模板")
            return self.templates["default"]
        
        # 如果default模板也不存在，抛出异常
        raise ValueError(f"模板 '{template_name}' 不存在")
    
    def get_template_list(self) -> Dict[str, Dict[str, str]]:
        """
        获取所有可用模板列表
        
        返回:
            模板信息字典，键为模板名称，值为模板信息
        """
        # 确保模板已发现
        if not self.templates:
            self._discover_templates()
        
        return {name: template.get_info() for name, template in self.templates.items()} 