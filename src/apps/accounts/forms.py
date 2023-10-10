from django import forms
from django.forms import widgets


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=widgets.PasswordInput)
