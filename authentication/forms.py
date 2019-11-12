from django import forms

class UserLoginForm(forms.Form):
 """user login form"""
 username = forms.CharField()
 password = forms.CharField(widget = forms.PasswordInput)