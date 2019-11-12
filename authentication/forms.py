from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
 """user login form"""
 username = forms.CharField()
 password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
  password1= forms.CharField(label="Password",
  widget=forms.PasswordInput)
  password2 = forms.CharField(
    label="Password Confirmation", 
    widget=forms.PasswordInput)

  class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']