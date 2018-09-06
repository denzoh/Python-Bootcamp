from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignupForm,LoginForm

def homepage(request):
    return render(request,'home.html')

def eggs(request):
    return HttpResponse('Eggs are Great!')

def signup(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
