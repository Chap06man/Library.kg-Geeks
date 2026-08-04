from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms 
from book.models import Book

def basket_creat(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form_obj = forms.BasketForm(request.POST, request.FILES)

        if form_obj.is_valid():
            basket = form_obj.save(commit=False)
            basket.choice_book = book
            basket.save()

            return redirect('book_list')
    else:
        form_obj = forms.BasketForm()

    return render(request, 'create_basket.html', {
        'form': form_obj,
        'book': book
    })

def read_basket_view(request):
    if request.method == 'GET':
        basket_list = models.BasketBook.objects.all()
    return render(request, 'read_basket.html', {'basket_list': basket_list})

#UPDATE
def update_basket_view(request, id):
    basket_id = get_object_or_404(models.BasketBook, id=id)
    if request.method == 'POST':
        form_obj = forms.TodoForm(request.POST, instance=basket_id)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/book_list/')
    else:
        form_obj = forms.TodoForm(instance=basket_id)
    return render(request, 'update_basket.html', {'form':form_obj, 'basket_id':basket_id})


#DELETE
def delete_basket_view(request, id):
    basket_id = get_object_or_404(models.BasketBook, id=id)
    basket_id.delete()
    return redirect('/book_list/')