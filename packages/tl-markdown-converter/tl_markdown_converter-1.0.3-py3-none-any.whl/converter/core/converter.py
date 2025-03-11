"""
主转换器模块

这个模块集成了所有转换功能，提供一键转换等高级功能。
"""

import os
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

from converter.utils.logger import logger
from converter.utils.config import config
from converter.utils.module_loader import module_loader

# 导入核心转换函数
# 注意：这里使用延迟导入，避免循环导入问题
def _import_converters():
    from converter.core.md_converter import convert_md_to_html, list_templates as _list_templates
    from converter.core.pdf_converter import convert_html_to_pdf
    from converter.core.image_converter import convert_html_to_image
    from converter.core.doc_converter import convert_md_to_doc, convert_html_to_doc
    
    return convert_md_to_html, convert_html_to_pdf, convert_html_to_image, _list_templates, convert_md_to_doc, convert_html_to_doc

def check_required_modules() -> bool:
    """
    检查所需模块是否存在
    
    返回:
        是否所有模块都存在
    """
    # 定义需要检查的模块和搜索路径
    required_modules = {
        "md_converter": ["converter/core"],
        "pdf_converter": ["converter/core"],
        "image_converter": ["converter/core"],
        "doc_converter": ["converter/core"]
    }
    
    # 检查模块是否存在
    all_exist, missing_modules = module_loader.check_required_modules(required_modules)
    
    if not all_exist:
        logger.error(f"缺少以下模块: {', '.join(missing_modules)}")
        logger.error("请确保这些模块存在于正确的路径中")
        return False
    
    return True

def convert_all(
    md_file: str, 
    output_dir: Optional[str] = None, 
    template: str = "default", 
    pdf_type: str = "both", 
    width: int = 720, 
    max_height: int = 4000,
    doc_options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    一键转换Markdown为所有格式
    
    参数:
        md_file: Markdown文件路径
        output_dir: 输出目录
        template: HTML模板名称
        pdf_type: PDF类型 (print, continuous, both)
        width: 图片宽度
        max_height: 单张图片最大高度
        doc_options: DOC转换选项
    
    返回:
        转换结果字典，包含各种格式的文件路径
    """
    # 导入转换函数
    convert_md_to_html, convert_html_to_pdf, convert_html_to_image, _, convert_md_to_doc, _ = _import_converters()
    
    if not os.path.exists(md_file):
        logger.error(f"找不到Markdown文件: {md_file}")
        return {"success": False}
    
    try:
        # 第一步：转换为HTML
        html_file = convert_md_to_html(md_file, output_dir, template)
        if not html_file:
            logger.error("Markdown转HTML失败，无法继续后续转换")
            return {"success": False}
        
        # 第二步：转换为PDF
        pdf_files = convert_html_to_pdf(html_file, output_dir, pdf_type)
        if not pdf_files:
            logger.warning("HTML转PDF失败")
            pdf_files = []
        
        # 第三步：转换为图片
        image_file = convert_html_to_image(html_file, output_dir, width, max_height)
        if image_file is False:
            logger.warning("HTML转图片失败")
            image_files = []
        else:
            image_files = [image_file]  # 封装为列表以保持现有API兼容性
        
        # 第四步：转换为DOC
        doc_file = convert_md_to_doc(md_file, output_dir, template, doc_options)
        if not doc_file:
            logger.warning("Markdown转DOC失败")
            doc_file = None
        
        # 返回转换结果
        return {
            "success": True,
            "html": html_file,
            "pdf": pdf_files if isinstance(pdf_files, list) else [],
            "image": image_files if isinstance(image_files, list) else [],
            "doc": doc_file
        }
    except Exception as e:
        logger.error(f"一键转换过程中出错: {str(e)}")
        import traceback
        logger.debug(traceback.format_exc())
        return {"success": False}

def list_templates() -> Dict[str, str]:
    """
    列出可用的HTML模板
    
    返回:
        模板字典，键为模板名称，值为模板描述
    """
    # 导入list_templates函数
    _, _, _, _list_templates, _, _ = _import_converters()
    return _list_templates() 