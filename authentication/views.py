from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from authentication.forms import UserLoginForm


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
    login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})