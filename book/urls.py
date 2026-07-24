from django.urls import path
from .views import MyFavouriteBook, AboutMySelf, MyHobby

urlpatterns = [
    path("book/", MyFavouriteBook),
    path("about/", AboutMySelf),
    path("hobby/", MyHobby),
]