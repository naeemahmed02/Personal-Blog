from django.contrib import admin
from django.utils.html import strip_tags
from .models import Comments

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['clean_comment', 'short_post_title', 'created_at', 'modified_at']

    def clean_comment(self, obj):
        return strip_tags(obj.comment_field)
    
    clean_comment.short_description = 'Comment'

    def short_post_title(self, obj):
        return obj.post.title[:100]
