from django.db import models
from froala_editor.fields import FroalaField
from category.models import ProjectsCategory

class Project(models.Model):
    project_title = models.CharField(max_length=300, unique=True)
    project_description = FroalaField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(ProjectsCategory, related_name='projects')
    featured_image = models.ImageField(upload_to='photos/project_category')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_title
