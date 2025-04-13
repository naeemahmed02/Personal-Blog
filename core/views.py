from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()[:5]
    return render(request, 'index.html',{'posts' : posts})

