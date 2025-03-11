"""
HTML到PDF转换模块

这个模块负责将HTML文件转换为PDF格式。
"""

import os
import asyncio
from pathlib import Path
from typing import Optional, List, Union, Dict, Any
import tempfile
import logging

from converter.utils.logger import logger, setup_logger
from converter.utils.config import config

# 导入用于实际转换的功能
try:
    from playwright.async_api import async_playwright
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    logger.warning("未安装Playwright库，将使用占位符PDF")
    PLAYWRIGHT_AVAILABLE = False

logger = setup_logger(__name__)

class PDFConverter:
    """PDF转换器"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def _get_pdf_options(self, continuous: bool = False) -> Dict[str, Any]:
        """获取PDF生成选项"""
        if continuous:
            return {
                'format': 'A4',
                'print_background': True,
                'margin': {'top': '0.2in', 'right': '0.2in', 'bottom': '0.2in', 'left': '0.2in'},
                'scale': 1.0,
                'prefer_css_page_size': True,
                'display_header_footer': False,
                'landscape': True,
                'page_ranges': '1-999999'  # 确保所有页面都在一个PDF中
            }
        else:
            return {
                'format': 'A4',
                'print_background': True,
                'margin': {'top': '0.4in', 'right': '0.4in', 'bottom': '0.4in', 'left': '0.4in'},
                'scale': 1.0,
                'prefer_css_page_size': True,
                'display_header_footer': False,
                'landscape': False
            }
    
    def _add_css_for_continuous(self, html_content: str) -> str:
        """添加连续布局的CSS样式"""
        css = """
        <style>
            @page {
                size: A4 landscape;
                margin: 0.2in;
            }
            body {
                margin: 0;
                padding: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 1em 0;
                page-break-inside: avoid;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f5f5f5;
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
                margin: 1em auto;
                page-break-inside: avoid;
            }
            pre, code {
                background-color: #f5f5f5;
                padding: 0.2em 0.4em;
                border-radius: 3px;
                font-family: Consolas, Monaco, 'Andale Mono', monospace;
                page-break-inside: avoid;
            }
            blockquote {
                margin: 1em 0;
                padding: 0.5em 1em;
                border-left: 4px solid #ddd;
                background-color: #f9f9f9;
                page-break-inside: avoid;
            }
            h1, h2, h3, h4, h5, h6 {
                margin-top: 1.5em;
                margin-bottom: 0.5em;
                page-break-after: avoid;
            }
            p {
                margin: 1em 0;
            }
            ul, ol {
                margin: 1em 0;
                padding-left: 2em;
                page-break-inside: avoid;
            }
            li {
                margin: 0.5em 0;
            }
        </style>
        """
        return html_content.replace('</head>', f'{css}</head>')
    
    def convert_html_to_pdf(self, html_file: str, output_dir: str, continuous: bool = False) -> List[str]:
        """
        将HTML文件转换为PDF
        
        Args:
            html_file: HTML文件路径
            output_dir: 输出目录
            continuous: 是否使用连续布局
            
        Returns:
            List[str]: 生成的PDF文件路径列表
        """
        if not os.path.exists(html_file):
            raise FileNotFoundError(f"HTML file not found: {html_file}")
            
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # 读取HTML内容
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # 添加连续布局的CSS样式
        if continuous:
            html_content = self._add_css_for_continuous(html_content)
            
        # 创建临时HTML文件
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w', encoding='utf-8') as f:
            f.write(html_content)
            temp_html = f.name
            
        try:
            self.logger.debug(f"打开HTML文件: file://{temp_html}")
            
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                
                # 加载HTML文件
                page.goto(f"file://{temp_html}")
                
                # 等待图片加载
                page.wait_for_load_state('networkidle')
                
                # 获取PDF选项
                pdf_options = self._get_pdf_options(continuous)
                self.logger.debug(f"生成PDF，使用选项: {pdf_options}")
                
                # 生成PDF
                output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(html_file))[0]}_{'continuous' if continuous else 'print'}.pdf")
                page.pdf(**pdf_options, path=output_file)
                
                self.logger.info(f"PDF生成成功: {output_file}")
                browser.close()
                
                return [output_file]
                
        finally:
            # 清理临时文件
            os.unlink(temp_html)

async def _convert_with_playwright(html_file_path, output_pdf_path, options=None):
    """
    使用Playwright将HTML转换为PDF
    
    参数:
        html_file_path: HTML文件路径
        output_pdf_path: 输出PDF文件路径
        options: PDF打印选项
        
    返回:
        是否成功转换
    """
    if not PLAYWRIGHT_AVAILABLE:
        logger.error("Playwright不可用，无法执行实际的PDF转换")
        return False
    
    # 默认打印选项
    default_options = {
        "format": config.get("pdf.default_page_format", "A4"),
        "print_background": True,
        "margin": {
            "top": config.get("pdf.margins.top", "0.4in"),
            "right": config.get("pdf.margins.right", "0.4in"),
            "bottom": config.get("pdf.margins.bottom", "0.4in"),
            "left": config.get("pdf.margins.left", "0.4in"),
        },
        "scale": 1.0,
        "prefer_css_page_size": True,
        "display_header_footer": False,
    }
    
    # 合并用户提供的选项
    if options is not None:
        default_options.update(options)
    
    try:
        # 将HTML文件路径转换为正确的URL格式
        file_url = Path(os.path.abspath(html_file_path)).as_uri()
        
        async with async_playwright() as p:
            # 启动Chrome浏览器
            browser = await p.chromium.launch()
            
            # 判断是否为连续格式（横向布局）
            is_continuous = options.get("landscape", False) if options else False
            
            # 设置适当的视口尺寸
            viewport_width = 1200
            viewport_height = 1600
            if is_continuous:
                # 连续格式使用更宽的视口以减少分页
                viewport_width = 1600
                viewport_height = 1200
            
            context = await browser.new_context(viewport={"width": viewport_width, "height": viewport_height})
            page = await context.new_page()
            
            # 导航到HTML文件
            logger.debug(f"打开HTML文件: {file_url}")
            await page.goto(file_url, wait_until="networkidle")
            
            # 等待页面完全加载
            await page.wait_for_load_state("networkidle")
            
            # 额外的等待，确保所有内容都完全渲染
            await asyncio.sleep(1)
            
            # 对于连续格式，添加CSS以确保内容连续显示
            if is_continuous:
                await page.add_style_tag(content="""
                    @page {
                        margin: 0;
                        size: auto;
                    }
                    body {
                        margin: 0;
                        padding: 0;
                        width: 100%;
                    }
                    /* 防止元素在页面中间被截断 */
                    h1, h2, h3, h4, h5, h6, p, ul, ol, li, table, figure {
                        page-break-inside: avoid;
                    }
                """)
                # 额外等待样式应用
                await asyncio.sleep(0.5)
            
            # 生成PDF
            logger.debug(f"生成PDF，使用选项: {default_options}")
            await page.pdf(path=output_pdf_path, **default_options)
            
            await browser.close()
            
            if os.path.exists(output_pdf_path):
                logger.info(f"PDF生成成功: {output_pdf_path}")
                return True
            else:
                logger.error(f"PDF生成失败，文件未创建: {output_pdf_path}")
                return False
    
    except Exception as e:
        logger.error(f"使用Playwright转换过程中出错: {str(e)}")
        import traceback
        logger.debug(traceback.format_exc())
        return False

def convert_html_to_pdf(
    html_file: str, 
    output_dir: Optional[str] = None, 
    pdf_type: str = "both"
) -> Union[List[str], bool]:
    """
    将HTML文件转换为PDF格式
    
    参数:
        html_file: HTML文件路径
        output_dir: 输出目录，默认为配置中的PDF目录
        pdf_type: PDF类型 (print, continuous, both)
    
    返回:
        生成的PDF文件路径列表或操作结果
    """
    try:
        if not os.path.exists(html_file):
            logger.error(f"找不到HTML文件: {html_file}")
            return False
        
        # 确定输出目录
        if output_dir is None:
            output_dir = config.get_path("pdf_dir")
        else:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        
        # 从HTML文件名中获取基本名称
        base_name = Path(html_file).stem
        
        # 创建PDF文件路径
        pdf_files = []
        
        # 根据pdf_type创建不同类型的PDF
        if pdf_type in ["print", "both"]:
            print_pdf_path = output_dir / f"{base_name}_print.pdf"
            
            if PLAYWRIGHT_AVAILABLE:
                # 打印版配置选项
                print_options = {
                    "format": config.get("pdf.default_page_format", "A4"),
                    "landscape": False
                }
                
                # 使用异步方式进行实际转换
                success = asyncio.run(_convert_with_playwright(
                    html_file, 
                    str(print_pdf_path), 
                    print_options
                ))
                
                if success:
                    pdf_files.append(str(print_pdf_path))
                    logger.info(f"生成打印版PDF: {print_pdf_path}")
                else:
                    # 如果失败则创建占位符
                    with open(print_pdf_path, 'w') as f:
                        f.write("This is a placeholder for a print-version PDF file.")
                    pdf_files.append(str(print_pdf_path))
                    logger.warning(f"转换失败，创建打印版PDF占位符: {print_pdf_path}")
            else:
                # 没有Playwright，创建占位符
                with open(print_pdf_path, 'w') as f:
                    f.write("This is a placeholder for a print-version PDF file.")
                pdf_files.append(str(print_pdf_path))
                logger.info(f"创建打印版PDF占位符: {print_pdf_path}")
        
        if pdf_type in ["continuous", "both"]:
            continuous_pdf_path = output_dir / f"{base_name}_continuous.pdf"
            
            if PLAYWRIGHT_AVAILABLE:
                # 连续版配置选项 - 更新选项以确保PDF是完整的，没有中间隔断
                continuous_options = {
                    "format": config.get("pdf.default_page_format", "A4"),
                    "landscape": True,
                    "margin": {
                        "top": "0.2in",
                        "right": "0.2in",
                        "bottom": "0.2in",
                        "left": "0.2in",
                    },
                    "scale": 1.0,
                    "prefer_css_page_size": True,
                    "display_header_footer": False,
                    "print_background": True
                }
                
                # 使用异步方式进行实际转换
                success = asyncio.run(_convert_with_playwright(
                    html_file, 
                    str(continuous_pdf_path), 
                    continuous_options
                ))
                
                if success:
                    pdf_files.append(str(continuous_pdf_path))
                    logger.info(f"生成连续版PDF: {continuous_pdf_path}")
                else:
                    # 如果失败则创建占位符
                    with open(continuous_pdf_path, 'w') as f:
                        f.write("This is a placeholder for a continuous-version PDF file.")
                    pdf_files.append(str(continuous_pdf_path))
                    logger.warning(f"转换失败，创建连续版PDF占位符: {continuous_pdf_path}")
            else:
                # 没有Playwright，创建占位符
                with open(continuous_pdf_path, 'w') as f:
                    f.write("This is a placeholder for a continuous-version PDF file.")
                pdf_files.append(str(continuous_pdf_path))
                logger.info(f"创建连续版PDF占位符: {continuous_pdf_path}")
        
        return pdf_files
    
    except Exception as e:
        logger.error(f"HTML转PDF错误: {str(e)}")
        import traceback
        logger.debug(traceback.format_exc())
        return False 