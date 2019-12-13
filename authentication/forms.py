from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """
    user login form
    """
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

"""
This ensures that the user has not already registered and that the form is valid
"""
def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
           raise forms.ValidationError(u'Email address is already registered')
        return email 


"""
This makes sure that the passwords match
"""
def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')

    if not password1 or not password2:
        raise ValidationError("Please confirm your password")

    if password1 != password2:
        raise ValidationErrror("Passwords do not match")

    return password2

"""
contact form
"""

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)