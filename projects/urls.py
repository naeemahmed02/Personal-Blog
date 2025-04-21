from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('<slug:project_slug>', views.project_detail, name = 'project_detail')

]