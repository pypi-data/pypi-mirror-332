#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
命令行接口模块

这个模块提供了命令行接口，用于处理命令行参数和调用相应的功能。
"""

import sys
import argparse
import os
from pathlib import Path
import traceback
import logging
import re

from converter.utils.logger import logger, setup_logger
from converter.utils.config import config
from converter.core.md_converter import convert_md_to_html, list_templates, MarkdownConverter, get_title_from_md
from converter.core.pdf_converter import convert_html_to_pdf
from converter.core.image_converter import convert_html_to_image
from converter.core.doc_converter import convert_md_to_doc
from converter.core.converter import convert_all, check_required_modules

def parse_args():
    """
    解析命令行参数
    
    Returns:
        argparse.Namespace: 解析后的参数
    """
    parser = argparse.ArgumentParser(description="Markdown格式转换工具")
    
    # 输入输出选项
    parser.add_argument("md_file", nargs="?", help="Markdown文件路径")
    parser.add_argument("--input-dir", "-i", help="输入目录，包含多个Markdown文件")
    parser.add_argument("--output-dir", "-o", help="输出目录")
    
    # 转换选项
    parser.add_argument("--html", action="store_true", help="转换为HTML格式")
    parser.add_argument("--pdf", action="store_true", help="转换为PDF格式")
    parser.add_argument("--image", action="store_true", help="转换为图片格式")
    parser.add_argument("--doc", action="store_true", help="转换为DOC格式")
    parser.add_argument("--all", action="store_true", help="转换为所有格式")
    
    # HTML选项
    parser.add_argument("--template", help="HTML模板名称")
    parser.add_argument("--html-file", help="HTML文件路径，用于转换其他格式")
    
    # 其他选项
    parser.add_argument("--list-templates", action="store_true", help="列出可用的HTML模板")
    parser.add_argument("--check", action="store_true", help="检查所需模块是否存在")
    parser.add_argument("--version", action="store_true", help="显示版本信息")
    parser.add_argument("--debug", action="store_true", help="启用调试模式")
    
    return parser.parse_args()

def main():
    """主函数"""
    args = parse_args()
    
    try:
        # 设置日志级别
        if args.debug:
            logging.getLogger().setLevel(logging.DEBUG)
            
        # 处理版本信息
        if args.version:
            print_version()
            return 0
            
        # 列出可用模板
        if args.list_templates:
            templates = list_templates()
            print("可用的HTML模板:")
            if not templates:
                print("  未找到任何模板")
            else:
                for template in templates:
                    print(f"  {template}")
            return 0
            
        # 检查所需模块
        if args.check:
            missing_modules = check_required_modules()
            if missing_modules:
                print("缺少以下模块:")
                for module in missing_modules:
                    print(f"  - {module}")
                return 1
            else:
                print("所有所需模块已安装")
                return 0
            
        # 验证必要参数
        if not args.md_file and not args.input_dir:
            logger.error("必须指定Markdown文件路径或输入目录")
            return 1
            
        if args.input_dir and not os.path.isdir(args.input_dir):
            logger.error(f"输入目录不存在: {args.input_dir}")
            return 1
            
        if args.md_file and not os.path.isfile(args.md_file):
            logger.error(f"Markdown文件不存在: {args.md_file}")
            return 1
            
        # 设置输出目录
        if args.output_dir:
            if not os.path.exists(args.output_dir):
                os.makedirs(args.output_dir)

        # 执行命令
        if args.html:
            html_file = convert_html(args)
            
            # 如果指定了其他转换，使用这个HTML文件作为输入
            if args.pdf:
                args.html_file = html_file
                convert_pdf(args)
                
            if args.image:
                args.html_file = html_file
                convert_image(args)
                
            if args.doc:
                args.html_file = html_file
                convert_doc(args)
        elif args.all:
            # 先生成HTML
            args.html = True
            html_file = convert_html(args)
            
            # 使用生成的HTML转换其他格式
            args.html_file = html_file
            
            # 生成DOC
            convert_doc(args)
            
            # 生成PDF
            convert_pdf(args)
            
            # 生成图片
            convert_image(args)
        else:
            # 单独的命令
            if args.pdf and args.html_file:
                convert_pdf(args)
                
            if args.image and args.html_file:
                convert_image(args)
                
            if args.doc and args.html_file:
                convert_doc(args)
                
        return 0
        
    except Exception as e:
        logger.error(f"程序执行出错: {str(e)}")
        if args.debug:
            import traceback
            logger.debug(traceback.format_exc())
        return 1

def post_process_html_file(html_file):
    """
    对HTML文件进行后处理，添加表格容器等
    
    Args:
        html_file: HTML文件路径
    """
    try:
        logger.debug(f"开始处理HTML文件：{html_file}")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 使用正则表达式查找所有表格并添加容器
        pattern = r'(<table>[\s\S]*?</table>)'
        replacement = r'<div class="table-container">\1</div>'
        
        # 检查是否找到表格
        if re.search(pattern, content):
            # 替换所有表格
            modified_content = re.sub(pattern, replacement, content)
            
            # 写回文件
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            logger.info(f"HTML后处理：已为{html_file}添加表格容器")
        else:
            logger.debug(f"HTML后处理：{html_file}中未找到表格标签")
    except Exception as e:
        logger.error(f"HTML后处理失败: {str(e)}")
        import traceback
        logger.debug(traceback.format_exc())

def convert_html(args):
    """处理HTML命令"""
    from converter.core.md_converter import MarkdownConverter, get_title_from_md
    converter = MarkdownConverter()
    
    html_dir = setup_output_dir(args.output_dir, "HTML")
    html_content = converter.convert_md_to_html(args.md_file, template=args.template or "default")
    
    # 保存HTML文件
    title = get_title_from_md(open(args.md_file, 'r', encoding='utf-8').read()) or os.path.splitext(os.path.basename(args.md_file))[0]
    # 替换文件名中的斜杠为下划线
    safe_title = title.replace('/', '_').replace('\\', '_')
    html_file = os.path.join(html_dir, f"{safe_title}.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    # 对HTML文件进行后处理
    post_process_html_file(html_file)
    
    logger.info(f"成功生成HTML文件: {html_file}")
    return html_file

def print_version():
    """打印版本信息"""
    from converter import __version__
    print(f"Markdown格式转换工具 v{__version__}")

def setup_output_dir(output_base, subdir):
    """
    设置输出目录
    
    Args:
        output_base: 基础输出目录
        subdir: 子目录名称
        
    Returns:
        str: 完整的输出目录路径
    """
    if output_base:
        output_dir = os.path.join(output_base, subdir)
    else:
        output_dir = subdir
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    return output_dir

def convert_pdf(args):
    """处理PDF命令"""
    from converter.core.pdf_converter import convert_html_to_pdf
    
    pdf_dir = setup_output_dir(args.output_dir, "PDF")
    pdf_files = convert_html_to_pdf(args.html_file, pdf_dir)
    
    if pdf_files:
        logger.info(f"成功生成PDF文件: {', '.join(pdf_files)}")
    else:
        logger.error("HTML转PDF失败")
    
    return pdf_files

def convert_image(args):
    """处理图片命令"""
    from converter.core.image_converter import convert_html_to_image
    
    image_dir = setup_output_dir(args.output_dir, "HTML_to_Image")
    image_file = convert_html_to_image(args.html_file, image_dir)
    
    if image_file:
        logger.info(f"成功生成图片文件: {image_file}")
    else:
        logger.error("HTML转图片失败")
    
    return image_file

def convert_doc(args):
    """处理DOC命令"""
    from converter.core.doc_converter import convert_html_to_doc
    
    doc_dir = setup_output_dir(args.output_dir, "DOC")
    doc_file = convert_html_to_doc(args.html_file, doc_dir)
    
    if doc_file:
        logger.info(f"成功生成DOC文件: {doc_file}")
    else:
        logger.error("HTML转DOC失败")
    
    return doc_file

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 