from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def MyFavouriteBook(request):
    return HttpResponse("Моя любимая книга - Samurai  без меча .")


def AboutMySelf(request):
    return HttpResponse("Меня зовут Сардорбек. Я изучаю Backend на Python и Django.")


def MyHobby(request):
    return HttpResponse("Мое хобби - АвтоСпорт.")