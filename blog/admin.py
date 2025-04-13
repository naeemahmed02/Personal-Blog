from django.contrib import admin
from .models import Post, Tags

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'modified_at']
    prepopulated_fields = {'slug' : ('title',)}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
