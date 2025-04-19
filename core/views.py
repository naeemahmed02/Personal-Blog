from django.shortcuts import render
from blog.models import Post
from utils.utils import generate_toc_and_content
from . models import PrivacyPolicy

def home(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'index.html',{'posts' : posts})

def privacy_policy(request):
    pri_policy = PrivacyPolicy.objects.all().order_by('-created_date').first()
    print(pri_policy)
    toc = generate_toc_and_content(pri_policy.policy_content)
    context = {
        'pri_policy': pri_policy,
        'toc': toc['toc'],
        'content_with_ids': toc['content'],
    }
    return render(request, 'privacy_policy.html', context)


def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def about_me(request):
    return render(request, 'about_me.html')

