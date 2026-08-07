from django.shortcuts import render , get_object_or_404
from . import models 
from django.http import HttpResponse
from django.core.paginator import Paginator
# 6-Домашка----------------------------------------------------------------------

def seacrh_view(request):
    query = request.GET.get('s', '')
    if query:
         book_list = models.Book.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Книга не найден')
    return render(request, 'book_list.html', {'book_list':book_list})


from django.db.models import F

def book_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        views_blog = request.session.get('viewed_book', [])

        if id not in views_blog:
            book_id.views = F("views") + 1
            book_id.save()
            book_id.refresh_from_db()

        views_blog.append(id)
        request.session['viewed_book'] = views_blog

    return render(request, 'book_detail.html', {'book_id': book_id})

# 2-домашка------------------------------------------------------------------

def book_list_view(request):
    if request.method == 'GET':
        #query - запрос
        book_list = models.Book.objects.all().order_by('-id')
        paginator = Paginator(book_list, 3)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
    return render(request, 'book_list.html', {'book_list': page_obj})

# Create your views here.----------------------------------------------------

def MyFavouriteBook(request):
    return HttpResponse("Моя любимая книга - Samurai  без меча .")


def AboutMySelf(request):
    return HttpResponse("Меня зовут Сардорбек. Я изучаю Backend на Python и Django.")


def MyHobby(request):
    return HttpResponse("Мое хобби - АвтоСпорт.")