from django.urls import path
from . import views

urlpatterns = [
    path("<str:category_slug>/<str:post_slug>", views.single_article, name = 'single_post'),
    path('articles', views.articles, name = 'articles'),
    path('articles/category/<slug:category>', views.articles, name='articles_by_category')

]