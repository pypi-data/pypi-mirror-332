/**
 * 文章模板脚本
 * 
 * 这个脚本提供以下功能：
 * 1. 自动生成文章目录
 * 2. 阅读进度指示器
 * 3. 目录折叠/展开功能
 * 4. 目录项高亮显示当前阅读位置
 */

document.addEventListener('DOMContentLoaded', function() {
    // 生成目录
    generateTableOfContents();
    
    // 设置进度条
    setupProgressBar();
    
    // 设置目录折叠/展开功能
    setupTocToggle();
    
    // 设置目录项高亮
    setupTocHighlight();
});

/**
 * 生成文章目录
 */
function generateTableOfContents() {
    const content = document.querySelector('.content');
    const tocContent = document.getElementById('toc-content');
    
    if (!content || !tocContent) return;
    
    // 查找所有标题元素
    const headings = content.querySelectorAll('h1, h2, h3, h4, h5, h6');
    
    if (headings.length === 0) {
        // 如果没有标题，隐藏目录
        const toc = document.getElementById('toc');
        if (toc) toc.style.display = 'none';
        return;
    }
    
    // 创建目录列表
    const tocList = document.createElement('ul');
    
    // 跟踪每个级别的最后一个列表
    const lastUl = {
        1: tocList,
        2: null,
        3: null,
        4: null,
        5: null,
        6: null
    };
    
    // 为每个标题创建目录项
    headings.forEach((heading, index) => {
        // 获取标题级别
        const level = parseInt(heading.tagName.substring(1));
        
        // 为标题添加ID，如果没有的话
        if (!heading.id) {
            heading.id = `heading-${index}`;
        }
        
        // 创建目录项
        const listItem = document.createElement('li');
        const link = document.createElement('a');
        link.href = `#${heading.id}`;
        link.textContent = heading.textContent;
        link.dataset.level = level;
        listItem.appendChild(link);
        
        // 将目录项添加到适当的列表中
        if (level === 1) {
            lastUl[1].appendChild(listItem);
            // 重置所有子级别
            lastUl[2] = lastUl[3] = lastUl[4] = lastUl[5] = lastUl[6] = null;
        } else {
            // 确保父级别的列表存在
            let parentLevel = level - 1;
            while (parentLevel > 0 && !lastUl[parentLevel]) {
                parentLevel--;
            }
            
            if (!lastUl[parentLevel]) {
                // 如果没有找到父级别，使用顶级列表
                lastUl[1].appendChild(listItem);
            } else {
                // 检查父级别的最后一个项目是否已经有子列表
                const parentLi = lastUl[parentLevel].lastElementChild;
                let childUl = parentLi.querySelector('ul');
                
                if (!childUl) {
                    // 如果没有子列表，创建一个
                    childUl = document.createElement('ul');
                    parentLi.appendChild(childUl);
                }
                
                // 将当前项目添加到子列表
                childUl.appendChild(listItem);
                lastUl[level] = childUl;
                
                // 重置所有子级别
                for (let i = level + 1; i <= 6; i++) {
                    lastUl[i] = null;
                }
            }
        }
    });
    
    // 将目录添加到页面
    tocContent.appendChild(tocList);
}

/**
 * 设置阅读进度条
 */
function setupProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    
    if (!progressBar) return;
    
    // 更新进度条
    function updateProgressBar() {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight - windowHeight;
        const scrollTop = window.scrollY;
        
        const progress = (scrollTop / documentHeight) * 100;
        progressBar.style.width = `${progress}%`;
    }
    
    // 初始更新
    updateProgressBar();
    
    // 滚动时更新
    window.addEventListener('scroll', updateProgressBar);
    window.addEventListener('resize', updateProgressBar);
}

/**
 * 设置目录折叠/展开功能
 */
function setupTocToggle() {
    const toggleButton = document.getElementById('toggle-toc');
    const toc = document.getElementById('toc');
    
    if (!toggleButton || !toc) return;
    
    // 检查本地存储中的状态
    const isTocCollapsed = localStorage.getItem('tocCollapsed') === 'true';
    
    // 应用初始状态
    if (isTocCollapsed) {
        toc.classList.add('collapsed');
    }
    
    // 切换目录显示状态
    toggleButton.addEventListener('click', function() {
        toc.classList.toggle('collapsed');
        
        // 保存状态到本地存储
        localStorage.setItem('tocCollapsed', toc.classList.contains('collapsed'));
    });
}

/**
 * 设置目录项高亮
 */
function setupTocHighlight() {
    const tocLinks = document.querySelectorAll('#toc-content a');
    
    if (tocLinks.length === 0) return;
    
    // 获取所有标题元素
    const headings = Array.from(document.querySelectorAll('.content h1, .content h2, .content h3, .content h4, .content h5, .content h6'));
    
    // 更新目录高亮
    function updateTocHighlight() {
        // 获取当前滚动位置
        const scrollPosition = window.scrollY + 100; // 添加偏移量以提前高亮
        
        // 找到当前可见的标题
        let currentHeading = null;
        
        for (let i = 0; i < headings.length; i++) {
            if (headings[i].offsetTop <= scrollPosition) {
                currentHeading = headings[i];
            } else {
                break;
            }
        }
        
        // 移除所有高亮
        tocLinks.forEach(link => {
            link.classList.remove('active');
        });
        
        // 如果找到当前标题，高亮对应的目录项
        if (currentHeading) {
            const currentLink = document.querySelector(`#toc-content a[href="#${currentHeading.id}"]`);
            if (currentLink) {
                currentLink.classList.add('active');
            }
        }
    }
    
    // 初始更新
    updateTocHighlight();
    
    // 滚动时更新
    window.addEventListener('scroll', updateTocHighlight);
} 