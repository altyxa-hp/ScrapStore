from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404

def index(request):
    categories = Category.objects.all()

    return render(request, 'index.html', {'categories' : categories})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })