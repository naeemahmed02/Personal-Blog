from django.contrib import admin
from .models import  Category, ProjectsCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'image']
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(ProjectsCategory)
class ProjectsCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name',]
    prepopulated_fields = {'category_slug': ('category_name',)}


