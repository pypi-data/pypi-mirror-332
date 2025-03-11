import os
import shutil
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class TemplateManager:
    """模板管理器"""
    
    def __init__(self, template_dir: Optional[str] = None):
        """
        初始化模板管理器
        
        Args:
            template_dir: 自定义模板目录路径，如果为None则使用默认内置模板
        """
        self.template_dir = template_dir or os.path.join(os.path.dirname(__file__), '..', 'templates')
        self._ensure_template_dir()
    
    def _ensure_template_dir(self):
        """确保模板目录存在"""
        if not os.path.exists(self.template_dir):
            os.makedirs(self.template_dir)
            logger.info(f"Created template directory: {self.template_dir}")
    
    def list_templates(self) -> List[str]:
        """列出所有可用的模板"""
        if not os.path.exists(self.template_dir):
            return []
            
        templates = []
        for item in os.listdir(self.template_dir):
            template_path = os.path.join(self.template_dir, item)
            if os.path.isdir(template_path):
                templates.append(item)
        return sorted(templates)
    
    def get_template_path(self, template_name: str) -> str:
        """
        获取指定模板的路径
        
        Args:
            template_name: 模板名称
            
        Returns:
            str: 模板目录的完整路径
        """
        template_path = os.path.join(self.template_dir, template_name)
        if not os.path.exists(template_path):
            raise ValueError(f"Template '{template_name}' not found in {self.template_dir}")
        return template_path
    
    def copy_template(self, template_name: str, target_dir: str) -> None:
        """
        复制模板文件到目标目录
        
        Args:
            template_name: 模板名称
            target_dir: 目标目录
        """
        template_path = self.get_template_path(template_name)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        # 复制模板文件
        for item in os.listdir(template_path):
            src = os.path.join(template_path, item)
            dst = os.path.join(target_dir, item)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
            elif os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
                
        logger.info(f"Copied template '{template_name}' to {target_dir}")
    
    def add_template(self, template_name: str, template_dir: str) -> None:
        """
        添加新的模板
        
        Args:
            template_name: 模板名称
            template_dir: 模板目录路径
        """
        if not os.path.exists(template_dir):
            raise ValueError(f"Template directory not found: {template_dir}")
            
        target_dir = os.path.join(self.template_dir, template_name)
        if os.path.exists(target_dir):
            raise ValueError(f"Template '{template_name}' already exists")
            
        shutil.copytree(template_dir, target_dir)
        logger.info(f"Added new template '{template_name}'")
    
    def remove_template(self, template_name: str) -> None:
        """
        删除模板
        
        Args:
            template_name: 模板名称
        """
        template_path = self.get_template_path(template_name)
        shutil.rmtree(template_path)
        logger.info(f"Removed template '{template_name}'") 