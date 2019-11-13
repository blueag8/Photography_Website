from django.shortcuts import render
from .models import Services
# Create your views here.

def all_products(request):
    services = Services.objects.all()
    return render(request, "services.html", {"services":services})