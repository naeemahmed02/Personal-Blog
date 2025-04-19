from django.contrib import admin
from . models import PrivacyPolicy

@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'updated_date']

