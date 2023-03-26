from django.urls import path, re_path
from .views import archive, get_article

urlpatterns = [
    path('', archive),
    re_path(r'^article/(?P<article_id>\d+)$', get_article, name='get_article')
    ]
