from django.shortcuts import render, reverse
from .models import Product
# Create your views here.

def product(request,id):  
    products = Product.objects.all()
    product = Product.objects.get(pk=id)
    print (product.name)
    return render(request, "product.html", {"id":id,"product":product})

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products, "product":product})

def portfolio(request):
    products = Product.objects.all()
    return render(request,"portfolio.html", {"products":products})

def image(request,id):  
    products = Product.objects.all()
    product = Product.objects.get(pk=id)
    return render(request,"image.html", {"id":id,"product":product, "products":products})



