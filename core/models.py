from django.db import models
from froala_editor.fields import FroalaField
import math
from django.utils.html import strip_tags

class PrivacyPolicy(models.Model):
    policy_content =            FroalaField()
    created_date =              models.DateTimeField(auto_now_add=True)
    updated_date =              models.DateTimeField(auto_now=True)

    def reading_time(self):
        word_count = len(strip_tags(self.policy_content,).split())
        return math.ceil(word_count / 200)

    def __str__(self):
        return f"Policy Date: {self.created_date.strftime('%Y-%m-%d')}"

class Resume(models.Model):

    # personal Information
    full_name =                 models.CharField(max_length=50,)
    job_title =                 models.CharField(max_length=100)
    summary =                   FroalaField()
    email =                     models.EmailField()
    phone_number =              models.CharField(max_length=15)
    location =                  models.CharField(max_length=200)
    profile =                   models.ImageField(upload_to='photos/resume', null=True, blank=True)

    # Social & Portfolio links
    linkedin_profile =          models.CharField(max_length=500, null=True, blank=True)
    git_hub_profile =           models.CharField(max_length=500, null=True, blank=True)
    personal_portfolio_or_website =        models.CharField(max_length=500, null=True, blank=True)
    twitter =                   models.CharField(max_length=500, null=True, blank=True)

    # Education

