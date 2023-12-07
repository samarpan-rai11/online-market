from django.urls import path
from . import views

app_name = 'item'    #for url template in html files

urlpatterns = [
    path('', views.items, name='items-search'),
    path('<int:pk>/', views.detail, name='product-detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('new/', views.new, name='new-item')
]