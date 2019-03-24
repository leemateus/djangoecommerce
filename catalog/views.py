from django.shortcuts import render

from .models import Product, Category

def product_list(request):
    produtos = Product.objects.all()

    return render(request, 'catalog/product_list.html',{'produtos':produtos})

def category(request, slug):
    category = Category.objects.get(slug=slug)
    categorias = {
        'current_category' : Category.objects.get(slug=slug),
        'produto' : Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', {'categorias' : categorias})
