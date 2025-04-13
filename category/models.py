from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=150, default='Unknown')
    image = models.ImageField(upload_to='photos/category_images', default='images/djangocentral_hero.svg')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


