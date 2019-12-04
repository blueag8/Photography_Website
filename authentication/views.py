from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.forms import UserLoginForm, UserRegistrationForm


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
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
       login_form = UserLoginForm(request.POST)

       if login_form.is_valid():
           user = auth.authenticate(username = request.POST['username'],
                                     password = request.POST['password'])

       if user:
            auth.login(user=user, request=request)
            messages.success(request, "Successfully logged in")
            return redirect(reverse('index'))

       else:
            login_form.add_error(None, "Username and/or Password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, "login.html", {"login_form": login_form})

def registration(request):
    """render registration page"""
    
    if request.user.is_authenticated:
       return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
          registration_form.save()

          user = auth.authenticate(username=request.POST['username'],
                                   password=request.POST['password1'])

          if user:
              auth.login(user=user, request=request)
              messages.success(request, "You have been successful")
              return redirect(reverse('index'))
          else:
              messages.error(request, "Sorry there has been a problem with registration")
              
    else:   
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', 
        {"registration_form": registration_form})

def user_profile(request):

    user = User.objects.get(email=request.user.email)

def contactUs(request):
    if request.method =="POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
           sender_name = contact_form.cleaned_data['name']
           sender_email = contact_form.cleaned_data['email']

           message = "{0} has sent you a new message:\n\n{1}".format(sender_name, contact_form.cleaned_data['message'])
           send_mail('New Enquiry', message, sender_email, ['ns.wickham08@outlook.com'])
           messages.success(request, "Message Sent")
           return redirect(reverse('index'))
    else:
        contact_form = ContactForm()
    return render(request, "contact.html", {'contact_form':contact_form})