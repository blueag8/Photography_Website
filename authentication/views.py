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
    if request.method == "POST":
       login_form = UserLoginForm(request.POST)

       if login_form.is_valid():
           user = auth.authenticate(username = request.POST['username'],
                                     password = request.POST['password'])

       if user:
            auth.login(user=user, request=request)
            messages.success(request, "Successfully logged in")

       else:
            login_form.add_error(None, "Username and/or Password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, "login.html", {"login_form": login_form})