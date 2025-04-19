from django.shortcuts import render, get_object_or_404, redirect
from . models import  Post
from utils.utils import generate_toc_and_content
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from comments.models import Comments
from django.contrib import messages


def single_article(request, category_slug, post_slug):
    single_post = get_object_or_404(Post, category__slug = category_slug, slug= post_slug)
    toc = generate_toc_and_content(single_post.content)

    if request.method == "POST":
        comment_content = request.POST.get('comment')

        if comment_content:
            Comments.objects.create(
                user = request.user,
                comment_field = comment_content,
                post = single_post
            )
            return redirect(request.path)
        else:
            messages.error(request, "Write something in the comment section.")
            return redirect(request.path + '#comment-section')
        

    context = context = {
    'single_post': single_post,
    'toc': toc['toc'],
    'content_with_ids': toc['content'],
}
    return render(request, 'post.html', context)

def articles(request):
    query = request.GET.get('q')  # 🔁 Corrected
    if query:
        articles = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)  # Optional: broaden search
        ).order_by('-created_at')
    else:
        articles = Post.objects.all().order_by('-created_at')  # 🔁 Added order_by for consistency

    paginator = Paginator(articles, settings.ARTICLE_PER_PAGE)
    page_number = request.GET.get('page')  # 🔁 Corrected
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj
    }
    return render(request, 'articles.html', context)


