/**
 * 博客模板JavaScript功能
 *
 * 提供博客模板的交互功能，包括返回顶部按钮、社交分享和评论功能
 */

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 初始化返回顶部按钮
    initBackToTop();
    
    // 初始化社交分享按钮
    initSocialShare();
    
    // 初始化评论表单
    initCommentForm();
    
    // 初始化代码高亮（如果有代码块）
    highlightCodeBlocks();
    
    // 生成目录（如果有[TOC]标记）
    generateTableOfContents();
});

/**
 * 初始化返回顶部按钮
 */
function initBackToTop() {
    var backToTopBtn = document.getElementById('back-to-top');
    if (!backToTopBtn) return;
    
    // 滚动时显示/隐藏按钮
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) { // 滚动超过300px时显示
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
    
    // 点击按钮时返回顶部
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // 平滑滚动
        });
    });
}

/**
 * 初始化社交分享按钮
 */
function initSocialShare() {
    var shareButtons = document.querySelectorAll('.share-btn');
    if (shareButtons.length === 0) return;
    
    // 获取当前页面信息
    var pageUrl = encodeURIComponent(window.location.href);
    var pageTitle = encodeURIComponent(document.title);
    
    // 为每个分享按钮添加点击事件
    shareButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var platform = this.getAttribute('data-platform');
            var shareUrl = '';
            
            // 根据平台生成分享链接
            switch(platform) {
                case 'weibo':
                    shareUrl = 'https://service.weibo.com/share/share.php?url=' + pageUrl + '&title=' + pageTitle;
                    break;
                case 'wechat':
                    // 微信分享通常需要生成二维码，这里简化处理
                    alert('请使用微信扫一扫，扫描当前页面分享');
                    return;
                case 'twitter':
                    shareUrl = 'https://twitter.com/intent/tweet?url=' + pageUrl + '&text=' + pageTitle;
                    break;
                case 'facebook':
                    shareUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + pageUrl;
                    break;
                case 'linkedin':
                    shareUrl = 'https://www.linkedin.com/shareArticle?mini=true&url=' + pageUrl + '&title=' + pageTitle;
                    break;
            }
            
            // 打开分享窗口
            if (shareUrl) {
                window.open(shareUrl, '_blank', 'width=600,height=450');
            }
        });
    });
}

/**
 * 初始化评论表单
 */
function initCommentForm() {
    var commentForm = document.getElementById('comment-form');
    if (!commentForm) return;
    
    commentForm.addEventListener('submit', function(e) {
        e.preventDefault(); // 阻止表单默认提交
        
        // 获取表单数据
        var name = document.getElementById('commenter-name').value;
        var email = document.getElementById('commenter-email').value;
        var content = document.getElementById('comment-content').value;
        
        // 简单验证
        if (!name || !email || !content) {
            alert('请填写所有必填字段');
            return;
        }
        
        // 这里应该发送评论数据到服务器
        // 由于这是静态模板，实际的提交逻辑需要根据具体后端实现
        alert('评论提交成功！');
        
        // 清空表单
        commentForm.reset();
    });
}

/**
 * 为代码块添加高亮
 */
function highlightCodeBlocks() {
    // 查找所有代码块
    var codeBlocks = document.querySelectorAll('pre code');
    if (codeBlocks.length === 0) return;
    
    // 如果页面中有highlight.js，则应用它
    if (typeof hljs !== 'undefined') {
        codeBlocks.forEach(function(block) {
            hljs.highlightBlock(block);
        });
    } else {
        // 简单的语法高亮（仅作为备选）
        codeBlocks.forEach(function(block) {
            // 为代码块添加行号
            var lines = block.innerHTML.split('\n');
            var numberedLines = lines.map(function(line, index) {
                return '<span class="line-number">' + (index + 1) + '</span>' + line;
            }).join('\n');
            
            // 应用行号和简单格式化
            block.innerHTML = numberedLines;
            block.classList.add('highlighted');
        });
    }
}

/**
 * 生成目录
 */
function generateTableOfContents() {
    // 查找[TOC]标记
    var content = document.querySelector('.markdown-body');
    if (!content) return;
    
    var tocPlaceholder = content.innerHTML.indexOf('[TOC]');
    if (tocPlaceholder === -1) return;
    
    // 查找所有标题
    var headings = content.querySelectorAll('h1, h2, h3, h4, h5, h6');
    if (headings.length === 0) return;
    
    // 创建目录容器
    var toc = document.createElement('div');
    toc.className = 'table-of-contents';
    toc.innerHTML = '<h3>目录</h3><ul></ul>';
    var tocList = toc.querySelector('ul');
    
    // 为每个标题创建目录项
    headings.forEach(function(heading, index) {
        // 为标题添加ID
        if (!heading.id) {
            heading.id = 'heading-' + index;
        }
        
        // 创建目录项
        var level = parseInt(heading.tagName.charAt(1));
        var listItem = document.createElement('li');
        listItem.style.marginLeft = (level - 1) * 20 + 'px';
        
        var link = document.createElement('a');
        link.href = '#' + heading.id;
        link.textContent = heading.textContent;
        
        listItem.appendChild(link);
        tocList.appendChild(listItem);
    });
    
    // 将[TOC]替换为生成的目录
    content.innerHTML = content.innerHTML.replace('[TOC]', toc.outerHTML);
} 