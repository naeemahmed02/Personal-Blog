from django.db import models
from froala_editor.fields import FroalaField
import math
from django.utils.html import strip_tags
from tinymce.models import HTMLField

class PrivacyPolicy(models.Model):
    policy_content =            HTMLField()
    created_date =              models.DateTimeField(auto_now_add=True)
    updated_date =              models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Policy'
        verbose_name_plural = 'Policies'

    def reading_time(self):
        word_count = len(strip_tags(self.policy_content,).split())
        return math.ceil(word_count / 200)
    

    def __str__(self):
        return f"Policy Date: {self.created_date.strftime('%Y-%m-%d')}"

