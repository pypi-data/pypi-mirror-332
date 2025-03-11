"""
模块加载器

这个模块提供了动态加载Python模块的功能。
"""

import importlib.util
import sys
import os
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

from converter.utils.logger import logger

class ModuleLoader:
    """模块加载器类，用于动态加载Python模块"""
    
    def __init__(self):
        self.loaded_modules = {}  # 缓存已加载的模块
    
    def load_module(self, module_path: str, module_name: Optional[str] = None) -> Optional[Any]:
        """
        从文件路径动态加载Python模块
        
        参数:
            module_path: 模块文件路径
            module_name: 模块名称，如果为None则使用文件名
        
        返回:
            加载的模块对象，如果加载失败则返回None
        """
        # 如果模块已加载，直接返回缓存的模块
        if module_path in self.loaded_modules:
            return self.loaded_modules[module_path]
        
        # 确保文件存在
        if not os.path.exists(module_path):
            logger.error(f"模块文件不存在: {module_path}")
            return None
        
        try:
            # 如果未指定模块名称，则使用文件名
            if module_name is None:
                module_name = Path(module_path).stem
            
            # 加载模块
            logger.debug(f"正在加载模块: {module_path} 作为 {module_name}")
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            if spec is None:
                logger.error(f"无法为文件创建模块规范: {module_path}")
                return None
                
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            
            # 缓存模块
            self.loaded_modules[module_path] = module
            
            return module
        except Exception as e:
            logger.error(f"加载模块 {module_path} 失败: {str(e)}")
            import traceback
            logger.debug(traceback.format_exc())
            return None
    
    def find_module(self, module_name: str, search_paths: List[str]) -> Optional[str]:
        """
        在指定的搜索路径中查找模块文件
        
        参数:
            module_name: 模块名称
            search_paths: 搜索路径列表
        
        返回:
            找到的模块文件路径，如果未找到则返回None
        """
        # 构建可能的文件名
        possible_filenames = [
            f"{module_name}.py",
            f"{module_name}/__init__.py"
        ]
        
        # 在搜索路径中查找模块
        for path in search_paths:
            for filename in possible_filenames:
                full_path = os.path.join(path, filename)
                if os.path.exists(full_path):
                    logger.debug(f"找到模块 {module_name} 在路径: {full_path}")
                    return full_path
        
        logger.warning(f"未找到模块 {module_name} 在搜索路径: {search_paths}")
        return None
    
    def check_required_modules(self, required_modules: Dict[str, List[str]]) -> Tuple[bool, List[str]]:
        """
        检查所需模块是否存在
        
        参数:
            required_modules: 字典，键为模块名称，值为搜索路径列表
        
        返回:
            (是否所有模块都存在, 缺失的模块列表)
        """
        missing_modules = []
        
        for module_name, search_paths in required_modules.items():
            module_path = self.find_module(module_name, search_paths)
            if module_path is None:
                missing_modules.append(module_name)
        
        return len(missing_modules) == 0, missing_modules

# 创建全局模块加载器实例
module_loader = ModuleLoader() 