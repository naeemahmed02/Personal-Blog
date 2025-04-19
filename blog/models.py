from django.db import models
from category.models import Category
import math
from django.utils.html import strip_tags
from froala_editor.fields import FroalaField
from django.urls import reverse


class Tags(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Post(models.Model):
    title =             models.CharField(max_length=300, unique=True)
    featured_image =    models.ImageField(upload_to='photos/featured_images')
    content =           FroalaField()
    slug =              models.SlugField(max_length=400, unique=True)
    # author =            models.CharField(max_length=50)
    category =          models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='posts')
    tags =              models.ManyToManyField(Tags, related_name='posts', blank=True)
    created_at =        models.DateTimeField(auto_now_add=True)
    modified_at =       models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def reading_time(self):
        word_count = len(strip_tags(self.content,).split())
        return math.ceil(word_count / 200)

    def get_url(self):
        return reverse('single_post', kwargs={
            'category_slug': self.category.slug,
            'post_slug' : self.slug
        })

    def __str__(self):
        return self.title

