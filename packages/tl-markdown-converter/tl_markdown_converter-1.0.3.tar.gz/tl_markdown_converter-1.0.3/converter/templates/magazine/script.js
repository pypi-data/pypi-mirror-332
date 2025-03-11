/**
 * 杂志风格模板的JavaScript功能
 */
document.addEventListener('DOMContentLoaded', function() {
    // 初始化所有功能
    addDropcapToFirstParagraph();
    enhanceImages();
    enhanceBlockquotes();
    addReadingProgressBar();
    setupLazyLoading();
    addTableOfContents();
});

/**
 * 为第一段添加首字下沉效果
 */
function addDropcapToFirstParagraph() {
    const content = document.querySelector('.magazine-content');
    if (!content) return;
    
    // 找到第一个段落
    const firstParagraph = content.querySelector('p');
    if (!firstParagraph) return;
    
    // 获取第一个字符并添加dropcap类
    const text = firstParagraph.textContent;
    if (text.length > 0) {
        const firstChar = text.charAt(0);
        const restOfText = text.substring(1);
        
        firstParagraph.innerHTML = `<span class="dropcap">${firstChar}</span>${restOfText}`;
    }
}

/**
 * 增强图片显示效果
 */
function enhanceImages() {
    const images = document.querySelectorAll('.magazine-content img');
    
    images.forEach(img => {
        // 为没有caption的图片添加caption容器
        if (!img.nextElementSibling || !img.nextElementSibling.classList.contains('image-caption')) {
            const alt = img.getAttribute('alt');
            if (alt && alt.trim() !== '') {
                const caption = document.createElement('div');
                caption.className = 'image-caption';
                caption.textContent = alt;
                img.parentNode.insertBefore(caption, img.nextSibling);
            }
        }
        
        // 添加点击放大效果
        img.addEventListener('click', function() {
            this.classList.toggle('expanded');
            if (this.classList.contains('expanded')) {
                this.style.cursor = 'zoom-out';
                this.style.maxWidth = '90vw';
                this.style.maxHeight = '90vh';
                this.style.position = 'relative';
                this.style.zIndex = '1000';
                this.style.transition = 'all 0.3s ease';
            } else {
                this.style.cursor = 'zoom-in';
                this.style.maxWidth = '100%';
                this.style.maxHeight = 'none';
                this.style.position = 'static';
                this.style.zIndex = 'auto';
            }
        });
        
        // 设置初始鼠标样式
        img.style.cursor = 'zoom-in';
    });
}

/**
 * 增强引用块的显示效果
 */
function enhanceBlockquotes() {
    const blockquotes = document.querySelectorAll('blockquote');
    
    blockquotes.forEach(quote => {
        // 添加引号装饰
        if (!quote.querySelector('.quote-marks')) {
            const quoteStart = document.createElement('span');
            quoteStart.className = 'quote-marks quote-start';
            quoteStart.innerHTML = '"';
            
            const quoteEnd = document.createElement('span');
            quoteEnd.className = 'quote-marks quote-end';
            quoteEnd.innerHTML = '"';
            
            quote.prepend(quoteStart);
            quote.append(quoteEnd);
        }
    });
}

/**
 * 添加阅读进度条
 */
function addReadingProgressBar() {
    // 创建进度条元素
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress-bar';
    progressBar.style.position = 'fixed';
    progressBar.style.top = '0';
    progressBar.style.left = '0';
    progressBar.style.height = '4px';
    progressBar.style.backgroundColor = '#000';
    progressBar.style.width = '0%';
    progressBar.style.zIndex = '1000';
    progressBar.style.transition = 'width 0.1s';
    
    document.body.appendChild(progressBar);
    
    // 监听滚动事件更新进度条
    window.addEventListener('scroll', function() {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight - windowHeight;
        const scrollTop = window.scrollY;
        
        const progress = (scrollTop / documentHeight) * 100;
        progressBar.style.width = progress + '%';
    });
}

/**
 * 设置图片懒加载
 */
function setupLazyLoading() {
    // 检查浏览器是否支持IntersectionObserver
    if ('IntersectionObserver' in window) {
        const lazyImages = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(function(image) {
            imageObserver.observe(image);
        });
    } else {
        // 回退方案：立即加载所有图片
        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(function(img) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        });
    }
}

/**
 * 添加目录
 */
function addTableOfContents() {
    const content = document.querySelector('.magazine-content');
    if (!content) return;
    
    // 查找所有标题
    const headings = content.querySelectorAll('h2, h3, h4');
    if (headings.length < 3) return; // 如果标题太少，不创建目录
    
    // 创建目录容器
    const toc = document.createElement('div');
    toc.className = 'table-of-contents';
    toc.innerHTML = '<h3>目录</h3>';
    
    const tocList = document.createElement('ul');
    toc.appendChild(tocList);
    
    // 为每个标题添加ID并创建目录项
    headings.forEach((heading, index) => {
        const id = `heading-${index}`;
        heading.id = id;
        
        const listItem = document.createElement('li');
        listItem.className = `toc-${heading.tagName.toLowerCase()}`;
        
        const link = document.createElement('a');
        link.href = `#${id}`;
        link.textContent = heading.textContent;
        
        listItem.appendChild(link);
        tocList.appendChild(listItem);
    });
    
    // 将目录插入到内容的开头
    const firstHeading = content.querySelector('h1, h2, h3, h4, h5, h6');
    if (firstHeading) {
        content.insertBefore(toc, firstHeading);
    } else {
        content.prepend(toc);
    }
    
    // 添加目录样式
    const style = document.createElement('style');
    style.textContent = `
        .table-of-contents {
            background-color: #f9f9f9;
            padding: 20px;
            margin: 20px 0 30px;
            border-left: 4px solid #000;
        }
        
        .table-of-contents h3 {
            margin-top: 0;
            margin-bottom: 15px;
        }
        
        .table-of-contents ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        .table-of-contents li {
            margin-bottom: 8px;
            font-size: 16px;
        }
        
        .table-of-contents a {
            text-decoration: none;
            color: #333;
            transition: color 0.2s;
        }
        
        .table-of-contents a:hover {
            color: #000;
            text-decoration: underline;
        }
        
        .toc-h3 {
            padding-left: 20px;
        }
        
        .toc-h4 {
            padding-left: 40px;
        }
    `;
    document.head.appendChild(style);
} 