"""
HTML到图片转换模块

这个模块负责将HTML文件转换为图片格式（单一完整图片）。
"""

import os
import asyncio
from pathlib import Path
from typing import Optional, List, Union

from converter.utils.logger import logger
from converter.utils.config import config

# 导入用于实际转换的功能
try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    logger.warning("未安装Playwright库，无法执行图片转换")
    PLAYWRIGHT_AVAILABLE = False

async def _convert_with_playwright(html_file_path, output_dir, base_name, width=720):
    """
    使用Playwright将HTML转换为单一完整图片
    
    参数:
        html_file_path: HTML文件路径
        output_dir: 输出目录
        base_name: 基本文件名
        width: 截图宽度
        
    返回:
        生成的图片文件路径
    """
    if not PLAYWRIGHT_AVAILABLE:
        logger.error("Playwright不可用，无法执行实际的图片转换")
        return None
    
    try:
        # 将HTML文件路径转换为URL格式
        file_url = Path(os.path.abspath(html_file_path)).as_uri()
        
        async with async_playwright() as p:
            # 启动浏览器
            browser = await p.chromium.launch()
            
            # 设置视口宽度
            context = await browser.new_context(viewport={"width": width, "height": 800})
            page = await context.new_page()
            
            # 导航到HTML文件
            logger.debug(f"打开HTML文件: {file_url}")
            await page.goto(file_url, wait_until="networkidle")
            
            # 等待页面完全加载
            await page.wait_for_load_state("networkidle")
            
            # 额外的等待，确保所有内容都完全渲染
            await asyncio.sleep(1)
            
            # 创建完整图片
            full_image_path = str(output_dir / f"{base_name}.png")
            await page.screenshot(path=full_image_path, full_page=True)
            logger.info(f"生成完整图片: {full_image_path}")
            
            await browser.close()
            
            return full_image_path
    
    except Exception as e:
        logger.error(f"使用Playwright进行图片转换时出错: {str(e)}")
        import traceback
        logger.debug(traceback.format_exc())
        return None

def convert_html_to_image(
    html_file: str, 
    output_dir: Optional[str] = None, 
    width: int = 720, 
    max_height: int = 4000  # 保留参数以兼容现有API，但不再使用
) -> Union[str, bool]:
    """
    将HTML文件转换为单一完整图片
    
    参数:
        html_file: HTML文件路径
        output_dir: 输出目录，默认为配置中的image_dir
        width: 图片宽度
        max_height: 参数保留但不再使用
    
    返回:
        生成的图片文件路径或操作结果(False表示失败)
    """
    try:
        if not os.path.exists(html_file):
            logger.error(f"找不到HTML文件: {html_file}")
            return False
        
        # 确定输出目录
        if output_dir is None:
            output_dir = config.get_path("image_dir")
        else:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        
        # 从HTML文件名中获取基本名称
        base_name = Path(html_file).stem
        
        if PLAYWRIGHT_AVAILABLE:
            # 使用Playwright进行实际转换
            image_file = asyncio.run(_convert_with_playwright(
                html_file, 
                output_dir, 
                base_name, 
                width=width
            ))
            
            if image_file:
                logger.info(f"成功生成图片: {image_file}")
                return image_file
            else:
                logger.error("图片转换失败")
                return False
        else:
            logger.error("无法执行图片转换：未安装Playwright库")
            return False
    
    except Exception as e:
        logger.error(f"HTML转图片错误: {str(e)}")
        import traceback
        logger.debug(traceback.format_exc())
        return False 