from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('privacy-policy', views.privacy_policy, name = 'privacy-policy'),
    path('terms-conditions', views.terms_conditions, name = 'terms-conditions'),
    path('about-me', views.about_me, name = 'about-me')

]