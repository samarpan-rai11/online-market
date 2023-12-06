from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'dashboard'   #for html files in url template

urlpatterns = [
    path('', views.index, name='index'),
]