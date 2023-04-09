from django.urls import path, re_path
from .views import archive, get_article, create_post

urlpatterns = [
    path('', archive),
    path('article/new/', create_post),
    re_path(r'^article/(?P<article_id>\d+)$', get_article),
    ]
