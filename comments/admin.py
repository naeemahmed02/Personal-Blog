from django.contrib import admin
from .models import Comments

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment_field', 'created_at', 'modified_at']
