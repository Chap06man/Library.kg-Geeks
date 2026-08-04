from django.urls import path
from .views import MyFavouriteBook, AboutMySelf, MyHobby
from . import views

urlpatterns = [
    path("book/", MyFavouriteBook),
    path("about/", AboutMySelf),
    path("hobby/", MyHobby),
    path('book_list/', views.book_list_view),
    path('book_list/<int:id>/', views.book_detail_view),
    path('book_list/', views.book_list_view, name='book_list'),
]
