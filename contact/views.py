from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import auth, messages
from .forms import ContactForm
from . import views

# Create your views here.
def contactUs(request):
    if request.method =="POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
           sender_name = contact_form.cleaned_data['name']
           sender_email = contact_form.cleaned_data['email']

           message = "{0} has sent you a new message:\n\n{1}".format(sender_name, contact_form.cleaned_data['message'])
           send_mail('New Enquiry', message, sender_email, ['ns.wickham08@outlook.com'])
           messages.success(request, "Message Sent")
           return redirect(reverse('contact'))
    else:
        contact_form = ContactForm()
    return render(request, "contact.html", {'contact_form':contact_form})

