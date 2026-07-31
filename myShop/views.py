from django.shortcuts import render
from . import models
# Create your views here.

def product_list_view(request):
    if request.method == "GET":
        prod = models.Product.objects.all()
        return render(request, 'prod_list.html', {'prod': prod})

def category_list_view(request):
    if request.method == "GET":
        caty = models.Category.objects.all()
        return render(request, 'caty_list.html', {'caty':caty})

def category_product(request, id):
    prod = models.Product.objects.filter(category_product_id=id)
    caty = models.Category.objects.get(id=id)

    return render(request,'caty_prod.html',{'prod': prod,'caty': caty})