from django.contrib import admin
from . models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'featured_image', 'created_date', 'updated_date']
    prepopulated_fields = {'slug' : ('project_title',)}

