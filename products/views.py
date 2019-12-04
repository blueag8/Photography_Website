from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    product = Product
    return render(request, "product.html", {"product.id":product.id} )

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})

def portfolio(request):
    products = Product.objects.all()
    return render(request,"portfolio.html", {"products":products})

