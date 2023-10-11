from django.shortcuts import render, redirect
from django import views
from . import forms
from django.contrib.auth import authenticate, login

# Create your views here.


class loginView(views.View):
    form_class = forms.LoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'accounts/login.html', {'form':form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, self.template_name, {'form':form})
        return render(request, self.template_name, {'form':form})   



