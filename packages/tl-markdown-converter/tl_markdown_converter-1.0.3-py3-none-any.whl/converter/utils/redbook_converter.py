#!/usr/bin/env python3
"""
小红书图片转换工具 - 将HTML转换为适合小红书的图片
支持自动分割长图片，确保每张图片高度不超过4000像素
优化段落边界检测 - 在合适的段落处分割内容
修复内容完整性问题 - 确保所有内容都被正确捕获
"""

import os
import sys
import argparse
import logging
from bs4 import BeautifulSoup
import re
import urllib.parse
import time
import math
import asyncio
from playwright.async_api import async_playwright

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("redbook_converter")

# 小红书图片格式配置
REDBOOK_WIDTH = 828  # 小红书图片宽度（像素）
REDBOOK_MAX_HEIGHT = 4000  # 小红书单张图片最大高度（像素）
REDBOOK_DEVICE_SCALE = 2.0  # 设备缩放比例，提高清晰度
MOBILE_WIDTH = 720        # 移动设备宽度（像素）

async def extract_title_from_html(page):
    """从HTML中提取标题"""
    title = await page.evaluate("""() => {
        // 尝试从h1标签获取标题
        const h1 = document.querySelector('h1');
        if (h1 && h1.textContent.trim()) {
            return h1.textContent.trim();
        }
        
        // 尝试从title标签获取标题
        const title = document.title;
        if (title && title.trim()) {
            return title.trim();
        }
        
        // 尝试从页面第一个大标题获取
        const heading = document.querySelector('h2, h3, h4, .title, .heading');
        if (heading && heading.textContent.trim()) {
            return heading.textContent.trim();
        }
        
        return "未命名文档";
    }""")
    
    return title

async def find_paragraph_boundary(page, target_position, direction="down", max_search=1000):
    """
    寻找页面中最接近目标位置的段落边界
    
    参数:
        page: playwright页面对象
        target_position: 目标Y坐标位置
        direction: 搜索方向，"up"向上搜索，"down"向下搜索
        max_search: 最大搜索范围
    
    返回:
        找到的边界位置Y坐标，如果未找到则返回None
    """
    # 使用JavaScript闭包直接在页面中访问变量
    js_code = f"""() => {{
        const targetY = {target_position};
        const direction = "{direction}";
        const maxSearch = {max_search};
        
        // 获取所有可能形成段落边界的元素
        const allElements = document.querySelectorAll('h1, h2, h3, h4, h5, p, div.chapter, div.section, hr, li, blockquote, figure, table');
        const boundaries = [];
        
        for (const el of allElements) {{
            const rect = el.getBoundingClientRect();
            const y = rect.top + window.scrollY;
            
            // 根据方向筛选边界
            if (direction === "up" && y < targetY) {{
                boundaries.push({{ y, element: el.tagName.toLowerCase() }});
            }} else if (direction === "down" && y > targetY) {{
                boundaries.push({{ y, element: el.tagName.toLowerCase() }});
            }}
        }}
        
        // 根据与目标位置的距离排序
        boundaries.sort((a, b) => {{
            return Math.abs(a.y - targetY) - Math.abs(b.y - targetY);
        }});
        
        // 返回最接近的边界（如果存在）
        return boundaries.length > 0 ? boundaries[0] : null;
    }}"""
    
    boundary_elements = await page.evaluate(js_code)
    
    if boundary_elements:
        logger.info(f"在位置{target_position}附近找到{direction}段落边界: {boundary_elements['y']} ({boundary_elements['element']})")
        return boundary_elements['y']
    
    logger.warning(f"未找到{direction}方向上的段落边界")
    return target_position

async def clip_screenshot(page, output_path, start_y, height, width):
    """
    截取页面指定区域的截图并保存到指定路径
    """
    try:
        # 确保所有参数为整数
        start_y = int(start_y)
        height = int(height)
        width = int(width)
        
        logger.info(f"尝试截取区域: start_y={start_y}, height={height}, width={width}")
        
        # 方法1：使用临时文件，先获取完整页面截图，然后裁剪需要的部分
        temp_path = f"{output_path}_temp.png"
        
        # 重置滚动位置并获取整个页面截图
        await page.evaluate("window.scrollTo(0, 0)")
        await page.screenshot(path=temp_path, full_page=True)
        
        # 使用Pillow裁剪指定区域
        from PIL import Image
        img = Image.open(temp_path)
        
        # 计算裁剪区域，考虑设备缩放比例
        device_pixel_ratio = await page.evaluate("window.devicePixelRatio")
        logger.info(f"设备像素比: {device_pixel_ratio}")
        
        # 根据设备像素比例调整坐标
        start_y_scaled = int(start_y * device_pixel_ratio)
        height_scaled = int(height * device_pixel_ratio)
        
        # 确保裁剪区域不超出图片边界
        img_width, img_height = img.size
        end_y_scaled = min(start_y_scaled + height_scaled, img_height)
        
        logger.info(f"裁剪区域(调整后): start_y={start_y_scaled}, end_y={end_y_scaled}, width={img_width}")
        
        # 裁剪图片并保存
        cropped_img = img.crop((0, start_y_scaled, img_width, end_y_scaled))
        cropped_img.save(output_path)
        logger.info(f"裁剪后的图片尺寸: {cropped_img.size}")
        
        # 删除临时文件
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
        return True
    except Exception as e:
        logger.error(f"截图过程中发生错误: {e}")
        
        # 尝试直接截取全页作为备用方案
        try:
            await page.screenshot(path=output_path, full_page=True)
            logger.warning("使用备用方案：保存了完整页面截图")
            return True
        except Exception as backup_error:
            logger.error(f"备用截图方案也失败: {backup_error}")
            return False

async def convert_html_to_redbook_images(html_file_path, width=720, max_height=4000, template_name="default"):
    """
    将HTML文件转换为小红书图片（宽度固定，高度分割）
    
    参数:
        html_file_path: HTML文件路径
        width: 生成图片的宽度，默认720像素
        max_height: 单张图片的最大高度，默认4000像素
        template_name: 模板名称，用于在文件名中标识
    """
    # 提取标题作为输出文件名
    base_name = os.path.basename(html_file_path)
    base_name = os.path.splitext(base_name)[0]
    
    # 创建输出目录
    output_dir = "HTML_to_Image"
    os.makedirs(output_dir, exist_ok=True)
    
    # 构造输出路径，添加模板名称
    if template_name and template_name.lower() != "default":
        output_base_path = os.path.join(output_dir, f"{base_name}_{template_name}")
    else:
        output_base_path = os.path.join(output_dir, base_name)
    
    output_full_path = f"{output_base_path}.png"
    
    logger.info(f"转换HTML文件: {html_file_path}")
    logger.info(f"使用模板: {template_name}")
    logger.info(f"输出路径: {output_full_path}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': width, 'height': 900},
            device_scale_factor=REDBOOK_DEVICE_SCALE
        )
        page = await context.new_page()
        
        try:
            # 打开HTML文件
            file_url = f"file://{os.path.abspath(html_file_path)}"
            await page.goto(file_url, wait_until="networkidle")
            
            # 提取标题
            title = await extract_title_from_html(page)
            logger.info(f"提取到标题: {title}")
            
            if title and title != "未命名文档":
                # 使用标题作为文件名（清理非法字符）
                safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
                
                # 在文件名中添加模板名称
                if template_name and template_name.lower() != "default":
                    output_base_path = os.path.join(output_dir, f"{safe_title}_{template_name}")
                else:
                    output_base_path = os.path.join(output_dir, safe_title)
                
                output_full_path = f"{output_base_path}.png"
                logger.info(f"使用标题作为文件名: {output_full_path}")
            
            # 获取页面总高度
            page_height = await page.evaluate("document.body.scrollHeight")
            logger.info(f"页面总高度: {page_height}像素")
            
            # 计算需要分成几张图片
            num_slices = math.ceil(page_height / max_height)
            
            if num_slices <= 1:
                # 如果不需要分割，直接保存完整图片
                logger.info(f"内容高度在限制范围内，直接保存完整图片: {output_full_path}")
                await page.screenshot(path=output_full_path, full_page=True)
            else:
                # 需要分割成多张图片
                logger.info(f"内容超出单张图片高度限制，将分割成{num_slices}张图片")
                
                # 计算每张图片的理想高度
                ideal_height = page_height / num_slices
                safe_height = ideal_height * 0.95  # 留一些余量，防止边界问题
                logger.info(f"每张图片理想高度约: {ideal_height:.2f}像素，安全高度约: {safe_height:.2f}像素")
                
                # 找到段落边界进行分割
                slice_boundaries = []
                previous_end = 0
                
                for i in range(1, num_slices):
                    target_y = i * ideal_height
                    
                    # 向下查找最近的段落边界
                    downward_boundary = await find_paragraph_boundary(page, target_y, direction="down")
                    # 向上查找最近的段落边界
                    upward_boundary = await find_paragraph_boundary(page, target_y, direction="up")
                    
                    # 选择离目标位置较近的边界
                    boundary = upward_boundary
                    boundary_type = "upward"
                    if downward_boundary and abs(downward_boundary - target_y) < abs(upward_boundary - target_y):
                        boundary = downward_boundary
                        boundary_type = "downward"
                    
                    if boundary:
                        logger.info(f"在位置{target_y}附近找到{boundary_type}段落边界: {boundary}")
                        slice_boundaries.append(boundary)
                        previous_end = boundary
                    else:
                        # 如果找不到合适的边界，使用估计值
                        logger.warning(f"在位置{target_y}附近未找到合适的段落边界，使用估计值")
                        slice_boundaries.append(target_y)
                        previous_end = target_y
                
                # 添加完整图片
                logger.info(f"保存完整图片到: {output_full_path}")
                await page.screenshot(path=output_full_path, full_page=True)
                
                # 根据段落边界分割图片
                slice_start = 0
                for i, slice_end in enumerate(slice_boundaries):
                    output_part_path = f"{output_base_path}_part{i+1}.png"
                    logger.info(f"分割图片{i+1}: 从 {slice_start} 到 {slice_end}，保存到: {output_part_path}")
                    
                    success = await clip_screenshot(page, output_part_path, slice_start, slice_end - slice_start, width)
                    if success:
                        logger.info(f"成功保存分割图片: {output_part_path}")
                    else:
                        logger.error(f"保存分割图片失败: {output_part_path}")
                    
                    slice_start = slice_end
                
                # 最后一个分片从最后一个边界到页面底部
                output_part_path = f"{output_base_path}_part{len(slice_boundaries)+1}.png"
                logger.info(f"分割图片{len(slice_boundaries)+1}: 从 {slice_start} 到 {page_height}，保存到: {output_part_path}")
                
                success = await clip_screenshot(page, output_part_path, slice_start, page_height - slice_start, width)
                if success:
                    logger.info(f"成功保存最后一个分割图片: {output_part_path}")
                else:
                    logger.error(f"保存最后一个分割图片失败: {output_part_path}")
            
            await browser.close()
            return True
                
        except Exception as e:
            logger.error(f"转换HTML到图片时出错: {str(e)}")
            import traceback
            traceback.print_exc()
            await browser.close()
            return False

def main():
    parser = argparse.ArgumentParser(description="将HTML文件转换为小红书格式图片")
    parser.add_argument("html_file", help="HTML文件路径")
    parser.add_argument("--width", type=int, default=MOBILE_WIDTH, help=f"图片宽度，默认{MOBILE_WIDTH}像素")
    parser.add_argument("--template", type=str, default="default", help="模板名称，将添加到输出文件名中")
    args = parser.parse_args()
    
    # 确认文件存在
    if not os.path.exists(args.html_file):
        logger.error(f"HTML文件不存在: {args.html_file}")
        return
    
    # 创建输出目录
    output_dir = "HTML_to_Image"
    os.makedirs(output_dir, exist_ok=True)
    
    # 转换为图片
    logger.info(f"转换为小红书格式图片（宽度{args.width}px，最大高度{REDBOOK_MAX_HEIGHT}px）...")
    success = asyncio.run(convert_html_to_redbook_images(
        html_file_path=args.html_file,
        width=args.width,
        max_height=REDBOOK_MAX_HEIGHT,
        template_name=args.template
    ))
    
    if success:
        logger.info(f"\n转换完成!")
        logger.info(f"图片文件保存在: {os.path.abspath(output_dir)}")
    else:
        logger.error(f"转换失败")

if __name__ == "__main__":
    main() 