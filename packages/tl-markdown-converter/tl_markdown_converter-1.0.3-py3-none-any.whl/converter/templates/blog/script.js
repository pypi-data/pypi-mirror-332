/**
 * 博客模板脚本
 * 
 * 这个脚本提供以下功能：
 * 1. 处理标签显示
 * 2. 处理相关文章链接
 * 3. 处理评论功能
 */

document.addEventListener('DOMContentLoaded', function() {
    // 处理标签显示
    processTags();
    
    // 处理相关文章链接
    processRelatedPosts();
    
    // 处理评论功能
    processComments();
});

/**
 * 处理标签显示
 */
function processTags() {
    const tagsContainer = document.querySelector('.tags-list');
    if (!tagsContainer) return;
    
    // 获取标签文本
    const tagsText = tagsContainer.textContent.trim();
    
    // 如果没有标签，隐藏标签区域
    if (!tagsText) {
        const tagsSection = document.querySelector('.post-tags');
        if (tagsSection) {
            tagsSection.style.display = 'none';
        }
        return;
    }
    
    // 清空容器
    tagsContainer.textContent = '';
    
    // 分割标签并创建标签元素
    const tags = tagsText.split(',').map(tag => tag.trim()).filter(tag => tag);
    
    tags.forEach(tag => {
        const tagElement = document.createElement('span');
        tagElement.className = 'tag';
        tagElement.textContent = tag;
        tagsContainer.appendChild(tagElement);
    });
}

/**
 * 处理相关文章链接
 */
function processRelatedPosts() {
    const relatedPostsContainer = document.querySelector('.related-posts-list');
    if (!relatedPostsContainer) return;
    
    // 获取相关文章文本
    const relatedPostsText = relatedPostsContainer.textContent.trim();
    
    // 如果没有相关文章，隐藏相关文章区域
    if (!relatedPostsText) {
        const relatedPostsSection = document.querySelector('.related-posts');
        if (relatedPostsSection) {
            relatedPostsSection.style.display = 'none';
        }
        return;
    }
    
    // 尝试解析JSON格式的相关文章
    try {
        const relatedPosts = JSON.parse(relatedPostsText);
        
        // 清空容器
        relatedPostsContainer.textContent = '';
        
        // 创建相关文章列表
        const list = document.createElement('ul');
        list.className = 'related-posts-items';
        
        relatedPosts.forEach(post => {
            const item = document.createElement('li');
            const link = document.createElement('a');
            link.href = post.url || '#';
            link.textContent = post.title || '未命名文章';
            item.appendChild(link);
            list.appendChild(item);
        });
        
        relatedPostsContainer.appendChild(list);
    } catch (e) {
        // 如果不是JSON格式，保留原始内容
        console.log('相关文章格式不是有效的JSON:', e);
    }
}

/**
 * 处理评论功能
 */
function processComments() {
    const commentsContainer = document.querySelector('.comments-container');
    if (!commentsContainer) return;
    
    // 获取评论文本
    const commentsText = commentsContainer.textContent.trim();
    
    // 如果没有评论，显示提示信息
    if (!commentsText) {
        commentsContainer.innerHTML = '<p class="no-comments">暂无评论</p>';
        return;
    }
    
    // 尝试解析JSON格式的评论
    try {
        const comments = JSON.parse(commentsText);
        
        // 清空容器
        commentsContainer.textContent = '';
        
        // 创建评论列表
        if (comments.length === 0) {
            commentsContainer.innerHTML = '<p class="no-comments">暂无评论</p>';
            return;
        }
        
        const list = document.createElement('ul');
        list.className = 'comments-list';
        
        comments.forEach(comment => {
            const item = document.createElement('li');
            item.className = 'comment-item';
            
            const header = document.createElement('div');
            header.className = 'comment-header';
            
            const author = document.createElement('span');
            author.className = 'comment-author';
            author.textContent = comment.author || '匿名';
            
            const date = document.createElement('span');
            date.className = 'comment-date';
            date.textContent = comment.date || '';
            
            header.appendChild(author);
            header.appendChild(date);
            
            const content = document.createElement('div');
            content.className = 'comment-content';
            content.textContent = comment.content || '';
            
            item.appendChild(header);
            item.appendChild(content);
            list.appendChild(item);
        });
        
        commentsContainer.appendChild(list);
    } catch (e) {
        // 如果不是JSON格式，保留原始内容
        console.log('评论格式不是有效的JSON:', e);
    }
}

/**
 * 检查作者链接并隐藏空链接
 */
window.addEventListener('load', function() {
    const authorLinks = document.querySelectorAll('.author-links a');
    
    authorLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (!href || href === '#' || href === '') {
            link.style.display = 'none';
        }
    });
    
    // 如果所有链接都被隐藏，隐藏整个链接容器
    const visibleLinks = document.querySelectorAll('.author-links a[style="display: none;"]');
    if (visibleLinks.length === authorLinks.length) {
        const linksContainer = document.querySelector('.author-links');
        if (linksContainer) {
            linksContainer.style.display = 'none';
        }
    }
}); 