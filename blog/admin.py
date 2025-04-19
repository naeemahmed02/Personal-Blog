from django.contrib import admin
from .models import Post, Tags
from froala_editor.widgets import FroalaEditor
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': FroalaEditor(),
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'modified_at']
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
