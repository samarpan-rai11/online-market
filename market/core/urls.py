from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LogInForm

app_name = 'core'    #for html files in url templates

urlpatterns = [
    path('', views.index),
    path('contact/',views.contact, name='contact1'),
    path('signup/',views.signup, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LogInForm), name='log-in'),
]