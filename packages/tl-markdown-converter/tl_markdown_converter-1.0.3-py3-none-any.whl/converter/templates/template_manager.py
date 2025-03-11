"""
模板管理器

这个模块负责扫描、发现和加载可用的模板。
"""

import os
import json
import logging
from pathlib import Path

# 配置日志
logger = logging.getLogger(__name__)


class TemplateBase:
    """模板基类，定义所有模板应实现的接口"""
    
    def __init__(self, template_dir, config):
        """
        初始化模板
        
        Args:
            template_dir: 模板目录路径
            config: 模板配置字典
        """
        self.template_dir = template_dir
        self.config = config
    
    def get_info(self):
        """获取模板基本信息"""
        return {
            'id': self.config.get('id', ''),
            'name': self.config.get('name', ''),
            'description': self.config.get('description', ''),
            'version': self.config.get('version', '1.0.0'),
            'author': self.config.get('author', '')
        }
    
    def get_html_template(self):
        """获取HTML模板文件路径"""
        return os.path.join(self.template_dir, self.config.get("html_template", "template.html"))
    
    def get_css_files(self):
        """获取CSS文件路径列表"""
        css_files = []
        for css_file in self.config.get("css_files", []):
            css_files.append(os.path.join(self.template_dir, css_file))
        return css_files
    
    def get_js_files(self):
        """获取JavaScript文件路径列表"""
        js_files = []
        for js_file in self.config.get("js_files", []):
            js_files.append(os.path.join(self.template_dir, js_file))
        return js_files
    
    def get_resources(self):
        """获取所有资源文件（CSS、JS等）"""
        resources = []
        resources.extend(self.get_css_files())
        resources.extend(self.get_js_files())
        return resources
    
    def get_pdf_settings(self):
        """获取PDF转换设置"""
        return self.config.get("pdf_settings", {})
    
    def get_image_settings(self):
        """获取图像转换设置"""
        return self.config.get("image_settings", {})
    
    def get_supported_features(self):
        """获取模板支持的特性"""
        return self.config.get("supported_features", [])


class TemplateManager:
    """模板管理器，负责扫描和加载模板"""
    
    def __init__(self, templates_dir):
        """
        初始化模板管理器
        
        Args:
            templates_dir: 模板目录路径
        """
        self.templates_dir = Path(templates_dir)
        self.available_templates = {}
        self.scan_templates()
    
    def scan_templates(self):
        """扫描并注册所有可用模板"""
        if not self.templates_dir.exists():
            logger.warning(f"模板目录不存在: {self.templates_dir}")
            return
        
        # 遍历templates目录下的所有子目录
        for template_dir in self.templates_dir.iterdir():
            if not template_dir.is_dir():
                continue
            
            # 检查配置文件是否存在 - 支持template.json和config.json两种文件名
            config_files = [template_dir / "template.json", template_dir / "config.json"]
            config_file = None
            
            for cf in config_files:
                if cf.exists():
                    config_file = cf
                    break
                    
            if not config_file:
                logger.warning(f"模板配置文件不存在: {template_dir}")
                continue
            
            try:
                # 读取配置文件
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                # 获取模板ID
                template_id = config.get('id', template_dir.name)
                
                # 注册模板
                self.available_templates[template_id] = {
                    'dir': str(template_dir),
                    'config': config,
                    'name': config.get('name', template_id),
                    'description': config.get('description', ''),
                    'version': config.get('version', '1.0.0'),
                    'author': config.get('author', '')
                }
                
                logger.info(f"已注册模板: {template_id}")
                
            except Exception as e:
                logger.error(f"加载模板配置失败: {config_file}, 错误: {str(e)}")
    
    def get_template_list(self):
        """
        返回可用模板列表及其描述
        
        Returns:
            dict: 模板ID到模板信息的映射
        """
        return {
            template_id: {
                'name': info['name'],
                'description': info['description'],
                'version': info['version'],
                'author': info['author']
            }
            for template_id, info in self.available_templates.items()
        }
    
    def load_template(self, template_name):
        """
        加载指定的模板
        
        Args:
            template_name: 模板ID或名称
            
        Returns:
            TemplateBase: 模板实例
            
        Raises:
            ValueError: 如果模板不存在
        """
        if template_name not in self.available_templates:
            # 尝试通过名称查找
            for template_id, info in self.available_templates.items():
                if info['name'] == template_name:
                    template_name = template_id
                    break
            else:
                # 如果仍未找到，使用默认模板
                if 'default' in self.available_templates:
                    logger.warning(f"模板 '{template_name}' 不存在，使用默认模板")
                    template_name = 'default'
                else:
                    raise ValueError(f"模板 '{template_name}' 不存在，且未找到默认模板")
        
        template_info = self.available_templates[template_name]
        return TemplateBase(template_info['dir'], template_info['config'])


def get_default_templates_dir():
    """获取默认模板目录路径"""
    # 首先尝试从当前工作目录查找
    cwd = Path.cwd()
    templates_dir = cwd / "templates"
    
    if templates_dir.exists() and templates_dir.is_dir():
        return templates_dir
    
    # 如果未找到，尝试从模块目录查找
    module_dir = Path(__file__).parent
    if module_dir.exists() and module_dir.is_dir():
        return module_dir
    
    # 最后返回当前工作目录下的templates
    return templates_dir 