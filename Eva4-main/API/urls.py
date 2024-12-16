# api/urls.py
from django.urls import path
from .views import list_products, create_product, update_product, destroy_product

urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('products/create/', create_product, name='create_product'),
    path('products/<pk>/update/', update_product, name='update_product'),
    path('products/<pk>/delete/', destroy_product, name='destroy_product'),
]