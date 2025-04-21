from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Comments
from django.contrib.auth.decorators import login_required
from accounts.decorators import comment_login_required

@comment_login_required
def post_comment(request, single_post):

    if request.method == "POST":
        comment_content = request.POST.get('comment')

        if comment_content:
            Comments.objects.create(
                user = request.user,
                comment_field = comment_content,
                post = single_post
            )
            return redirect(request.path + '#comment-section')
        else:
            messages.error(request, "Write something in the comment section.")
            return redirect(request.path + '#comment-section')