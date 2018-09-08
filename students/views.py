from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def eggs(request):
    return HttpResponse('Eggs are Great!')

# class SignupView(TemplateView):
#     template_name = 'templates/signup.html'
#
#     def get(self, request, *args, **kwargs):
#         form = SignupForm()
#         return super(SignupView,self).get(request,signup_form=form)
#
#     def post(self,request, *args, **kwargs):
#
#         form = SignupForm(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=username,email=email,password=password)
#
#         return super(SignupView,self).get(request,signup_form=form)
def signup(request):
    if request.method == 'POST':#user has info and wants account now
        if request.POST.get('password')==request.POST.get('confirm_password'):
            try:
                user = User.objects.get(username=request.POST.get('username'))
                return render(request, 'signup.html',{'error':'User name is taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST.get('username'),password = request.POST.get('password'))
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'form': SignupForm},{'error':'Passwords do not match'})
    else:
        form = SignupForm(request.POST)
        return render(request, 'signup.html', {'form': SignupForm})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': LoginForm})

    else:

        form = LoginForm()
        return render(request, 'login.html', {'form': LoginForm})

def account_logout(request):
    logout(request)
    url = reverse('students:login')
    return redirect(url,args=(),kwargs={})
