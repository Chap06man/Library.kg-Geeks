from django.shortcuts import render , get_object_or_404
from . import models
from django.http import HttpResponse

# 2-домашка------------------------------------------------------------------

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})

def book_list_view(request):
    if request.method == 'GET':
        #query - запрос
        book_list = models.Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'book_list': book_list})

# Create your views here.----------------------------------------------------

def MyFavouriteBook(request):
    return HttpResponse("Моя любимая книга - Samurai  без меча .")


def AboutMySelf(request):
    return HttpResponse("Меня зовут Сардорбек. Я изучаю Backend на Python и Django.")


def MyHobby(request):
    return HttpResponse("Мое хобби - АвтоСпорт.")