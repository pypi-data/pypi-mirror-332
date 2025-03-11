/**
 * 学术风格模板的JavaScript函数
 */

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 为所有标题添加ID，方便引用
    addIdsToHeadings();
    
    // 处理交叉引用
    processCrossReferences();
    
    // 生成目录
    generateTableOfContents();
    
    // 处理图表标注
    processTableAndFigureCaptions();
});

/**
 * 为所有标题添加ID
 */
function addIdsToHeadings() {
    const headings = document.querySelectorAll('h2, h3, h4, h5, h6');
    headings.forEach(function(heading, index) {
        if (!heading.id) {
            const id = 'section-' + (index + 1);
            heading.id = id;
        }
    });
}

/**
 * 处理文档中的交叉引用
 */
function processCrossReferences() {
    const refs = document.querySelectorAll('a.ref');
    refs.forEach(function(ref) {
        const target = ref.getAttribute('href');
        if (target && target.startsWith('#')) {
            const targetElement = document.querySelector(target);
            if (targetElement) {
                // 如果是图表引用，添加图表编号
                if (targetElement.classList.contains('figure') || 
                    targetElement.tagName.toLowerCase() === 'figure') {
                    const figures = document.querySelectorAll('figure, .figure');
                    const figureIndex = Array.from(figures).indexOf(targetElement) + 1;
                    ref.textContent = `图 ${figureIndex}`;
                }
                // 如果是表格引用，添加表格编号
                else if (targetElement.classList.contains('table') || 
                         targetElement.tagName.toLowerCase() === 'table') {
                    const tables = document.querySelectorAll('table, .table');
                    const tableIndex = Array.from(tables).indexOf(targetElement) + 1;
                    ref.textContent = `表 ${tableIndex}`;
                }
                // 如果是章节引用，添加章节编号
                else if (targetElement.tagName.match(/^H[2-6]$/i)) {
                    const headingLevel = parseInt(targetElement.tagName.charAt(1));
                    const headings = document.querySelectorAll(`h${headingLevel}`);
                    const headingIndex = Array.from(headings).indexOf(targetElement) + 1;
                    ref.textContent = `${headingIndex} 节`;
                }
            }
        }
    });
}

/**
 * 生成目录
 */
function generateTableOfContents() {
    const tocElement = document.getElementById('toc');
    if (!tocElement) return;
    
    const headings = document.querySelectorAll('h2, h3, h4');
    if (headings.length === 0) {
        tocElement.style.display = 'none';
        return;
    }
    
    const tocList = document.createElement('ul');
    tocList.className = 'toc-list';
    
    let currentLevel = 2;
    let currentList = tocList;
    let listStack = [tocList];
    
    headings.forEach(function(heading) {
        const level = parseInt(heading.tagName.charAt(1));
        
        // 如果当前标题级别大于上一个，创建新的子列表
        if (level > currentLevel) {
            const newList = document.createElement('ul');
            currentList.lastChild.appendChild(newList);
            listStack.push(newList);
            currentList = newList;
        }
        // 如果当前标题级别小于上一个，回到相应的父列表
        else if (level < currentLevel) {
            const stepsUp = currentLevel - level;
            for (let i = 0; i < stepsUp; i++) {
                listStack.pop();
            }
            currentList = listStack[listStack.length - 1];
        }
        
        const listItem = document.createElement('li');
        const link = document.createElement('a');
        link.href = '#' + heading.id;
        link.textContent = heading.textContent;
        listItem.appendChild(link);
        currentList.appendChild(listItem);
        
        currentLevel = level;
    });
    
    tocElement.appendChild(tocList);
}

/**
 * 处理图表标注
 */
function processTableAndFigureCaptions() {
    // 处理图片标注
    const figures = document.querySelectorAll('figure');
    figures.forEach(function(figure, index) {
        const caption = figure.querySelector('figcaption');
        if (caption) {
            caption.innerHTML = `图 ${index + 1}：${caption.innerHTML}`;
        }
    });
    
    // 处理表格标注
    const tables = document.querySelectorAll('table');
    tables.forEach(function(table, index) {
        const caption = table.querySelector('caption');
        if (caption) {
            caption.innerHTML = `表 ${index + 1}：${caption.innerHTML}`;
        }
    });
} 