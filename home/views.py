from django.shortcuts import render

# Create your views here.
def index(request):
    """A view for home page"""
    return render(request, "index.html")

def about(request):
    """A view for the about page"""
    return render(request, "about.html")

