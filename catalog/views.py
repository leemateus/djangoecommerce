from django.shortcuts import render

from .models import Product

def product_list(request):
    produtos = Product.objects.all()

    return render(request, 'product_list.html',{'produtos':produtos})
