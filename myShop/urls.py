# myShop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list_view, name='categories'),
    path('products/', views.product_list_view, name='products'),
    path('category/<int:id>/', views.category_product, name='category_products'),
]