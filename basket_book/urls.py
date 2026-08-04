from django.urls import path
from . import views

urlpatterns = [
    path('basket/create/<int:book_id>/', views.basket_creat, name='create_basket'),

    path('read/', views.read_basket_view, name='basket_list'),

    path('book_list/<int:id>/update/', views.update_basket_view),
    path('book_list/<int:id>/delete/', views.delete_basket_view),
]