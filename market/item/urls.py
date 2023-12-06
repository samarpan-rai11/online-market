from django.urls import path
from . import views

app_name = 'item'    #for url template in html files

urlpatterns = [
    path('<int:pk>/', views.detail, name='product-detail'),
    path('new/', views.new, name='new-item')
]