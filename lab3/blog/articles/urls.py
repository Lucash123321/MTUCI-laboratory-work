from django.urls import path
from .views import archive

urlpatterns = [
    path('', archive),
    ]