from django.shortcuts import render
from .models import Products
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})