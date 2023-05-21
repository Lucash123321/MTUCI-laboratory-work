from django.urls import path, re_path
from .views import archive, get_article, create_post, register, authorize
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', archive, name='main'),
    path('article/new/', create_post),
    re_path(r'^article/(?P<article_id>\d+)$', get_article),
    path('register/', register),
    path('logout/', LogoutView.as_view(), {'next_page': '/'}),
    path('authorize/', authorize)
    ]
