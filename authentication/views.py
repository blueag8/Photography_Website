from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


# Create your views here.
def index(request):
    """return home page"""
    return render(request, "index.html")

def logout(request):
   """logout"""
   auth.logout(request)
   messages.success(request, "You have been successfully logged out")
   return redirect(reverse("index"))

def login(request):
    """return user login"""
    return render(request, "login.html")