"""
Markdown到HTML转换模块

这个模块负责将Markdown文件转换为HTML格式。
"""

import os
import re
import json
from pathlib import Path
from typing import Optional, Dict, List, Any
import datetime
import logging

import markdown
from markdown import Markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from converter.utils.logger import logger, setup_logger
from converter.utils.config import config

# 导入模板管理器
from converter.templates import TemplateManager, get_default_templates_dir

# 初始化模板管理器
def get_template_manager():
    """获取模板管理器实例"""
    templates_dir = get_default_templates_dir()
    return TemplateManager(templates_dir)

def get_title_from_md(md_content: str) -> Optional[str]:
    """
    从Markdown内容中提取标题
    
    参数:
        md_content: Markdown内容
    
    返回:
        提取的标题，如果未找到则返回None
    """
    # 查找第一个一级标题 (# 标题)
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # 如果没有找到一级标题，尝试查找YAML前置元数据中的title字段
    yaml_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', md_content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        title_match = re.search(r'title:\s*(.+)$', yaml_content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
    
    return None

def extract_yaml_metadata(md_content: str) -> Dict[str, Any]:
    """
    从Markdown内容中提取YAML前置元数据
    
    参数:
        md_content: Markdown内容
    
    返回:
        提取的元数据字典
    """
    metadata = {}
    yaml_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', md_content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        for line in yaml_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
    
    return metadata

def list_templates() -> List[str]:
    """
    列出所有可用的模板
    
    返回:
        模板名称列表
    """
    template_manager = get_template_manager()
    template_list = template_manager.get_template_list()
    
    # 返回模板名称列表，按字母顺序排序
    templates = []
    for template_id, info in template_list.items():
        template_name = info.get('name', template_id)
        template_desc = info.get('description', '')
        templates.append(f"{template_id} - {template_name}: {template_desc}")
    
    return sorted(templates)

class MarkdownConverter:
    """Markdown转换器类"""
    
    def __init__(self):
        """初始化转换器"""
        self.template_manager = get_template_manager()
        
    def convert_md_to_html(self, md_file: str, template: str = "default", options: Dict[str, Any] = None) -> str:
        """
        将Markdown文件转换为HTML
        
        参数:
            md_file: Markdown文件路径
            template: 模板名称
            options: 模板选项
            
        返回:
            生成的HTML内容
        """
        # 读取Markdown文件
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        # 提取元数据
        metadata = self._extract_yaml_metadata(md_content)
        
        # 提取标题
        title = self._get_title_from_md(md_content) or os.path.splitext(os.path.basename(md_file))[0]
        
        # 创建Markdown解析器
        md = Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.meta',
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.nl2br',
            'markdown.extensions.sane_lists',
        ])
        
        # 转换Markdown为HTML
        html_content = md.convert(md_content)
        
        try:
            # 加载模板
            template_obj = self.template_manager.load_template(template)
            template_path = template_obj.get_html_template()
            template_dir = template_path.parent
            template_file = template_path.name
            
            # 创建Jinja2环境
            env = Environment(
                loader=FileSystemLoader(str(template_dir)),
                autoescape=False  # 禁用自动转义
            )
            template = env.get_template(template_file)
            
            # 准备模板变量
            template_vars = {
                'title': title,
                'content': html_content,
                'metadata': metadata,
                'date': datetime.datetime.now().strftime('%Y-%m-%d'),
                'time': datetime.datetime.now().strftime('%H:%M:%S'),
            }
            
            # 添加用户提供的选项
            if options:
                template_vars.update(options)
            
            # 渲染模板
            return template.render(**template_vars)
            
        except Exception as e:
            logger.error(f"Template rendering failed: {str(e)}")
            # 如果模板渲染失败，返回基本的HTML
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>{title}</title>
                <style>
                    body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 1rem; }}
                    pre {{ background: #f6f8fa; padding: 1rem; overflow-x: auto; }}
                    code {{ background: #f6f8fa; padding: 0.2rem 0.4rem; border-radius: 3px; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f6f8fa; }}
                </style>
            </head>
            <body>
                <h1>{title}</h1>
                {html_content}
            </body>
            </html>
            """
    
    def _extract_yaml_metadata(self, content: str) -> Dict[str, Any]:
        """提取YAML元数据"""
        metadata = {}
        if content.startswith('---'):
            try:
                end = content.find('---', 3)
                if end != -1:
                    yaml_text = content[3:end].strip()
                    metadata = yaml.safe_load(yaml_text) or {}
            except Exception as e:
                logger.warning(f"Failed to parse YAML metadata: {str(e)}")
        return metadata
    
    def _get_title_from_md(self, content: str) -> Optional[str]:
        """从Markdown内容中提取标题"""
        # 尝试从元数据中获取标题
        metadata = self._extract_yaml_metadata(content)
        if metadata and 'title' in metadata:
            return metadata['title']
        
        # 尝试从第一个标题获取
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                return line[2:].strip()
        return None

def convert_md_to_html(md_file: str, template: str = "default", options: Dict[str, Any] = None) -> str:
    """
    将Markdown文件转换为HTML
    
    参数:
        md_file: Markdown文件路径
        template: 模板名称
        options: 模板选项
        
    返回:
        生成的HTML内容
    """
    converter = MarkdownConverter()
    return converter.convert_md_to_html(md_file, template, options)

def convert_md_dir_to_html(input_dir: str, output_dir: str, template: str = "default", template_options: Dict[str, Any] = None) -> List[str]:
    """
    将目录中的所有Markdown文件转换为HTML
    
    参数:
        input_dir: 输入目录
        output_dir: 输出目录
        template: 模板名称
        template_options: 模板选项
        
    返回:
        生成的HTML文件路径列表
    """
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 查找所有Markdown文件
    md_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith((".md", ".markdown")):
                md_files.append(os.path.join(root, file))
    
    # 转换所有Markdown文件
    html_files = []
    for md_file in md_files:
        # 生成输出文件路径
        rel_path = os.path.relpath(md_file, input_dir)
        html_filename = os.path.splitext(rel_path)[0] + ".html"
        html_path = os.path.join(output_dir, html_filename)
        
        # 确保输出目录存在
        html_dir = os.path.dirname(html_path)
        if not os.path.exists(html_dir):
            os.makedirs(html_dir)
        
        # 转换文件
        html_content = convert_md_to_html(md_file, template, template_options)
        
        # 写入HTML文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        html_files.append(html_path)
    
    return html_files 