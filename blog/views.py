from django.shortcuts import render, get_object_or_404, redirect
from . models import  Post
from utils.utils import generate_toc_and_content
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from comments.views import post_comment


def single_article(request, category_slug, post_slug):
    single_post = get_object_or_404(Post, category__slug = category_slug, slug= post_slug)
    toc = generate_toc_and_content(single_post.content)

    post_comment(request, single_post=single_post)

    context = context = {
    'single_post': single_post,
    'toc': toc['toc'],
    'content_with_ids': toc['content'],
}
    return render(request, 'post.html', context)

def articles(request, category = None):

    articles = Post.objects.all()

    query = request.GET.get('q')

    if category:
        articles = articles.filter(category__slug=category)
    
    if query:
        articles = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        
    else:
        articles = articles.order_by('-created_at')


    paginator = Paginator(articles, settings.ARTICLE_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
        'selected_category' : category
    }
    return render(request, 'articles.html', context)


