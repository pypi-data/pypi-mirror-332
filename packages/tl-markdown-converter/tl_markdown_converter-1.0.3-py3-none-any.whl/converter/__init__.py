"""
文章格式转换工具包

这个包提供了一套工具，用于将Markdown文档转换为HTML、PDF、图片和DOC格式。
"""

__version__ = '1.0.3'
__author__ = 'tieli'

# 导入主要模块，使它们可以直接从包中导入
from converter.core.md_converter import convert_md_to_html
from converter.core.pdf_converter import convert_html_to_pdf
from converter.core.image_converter import convert_html_to_image
from converter.core.doc_converter import convert_md_to_doc, convert_html_to_doc
from converter.core.converter import convert_all, list_templates 