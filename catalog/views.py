from django.shortcuts import render

from .models import Product, Category

def product_list(request):
    produtos = Product.objects.all()

    return render(request, 'catalog/product_list.html',{'produtos':produtos})

def category(request, slug):
    category = Category.objects.get(id=slug)
    produtos = Product.objects.filter(category__id=slug)
    result = {
        'current_category' : category,
        'produto' : Product.objects.filter(category__id=slug),
    }
    return render(request, 'catalog/category.html', {'result' : result, 'produtos': produtos})

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'catalog/product.html', {'product' : product})
