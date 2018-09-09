from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import CreateUser

# Create your views here.
def home(request):
    return HttpResponse('Eggs are Great!')

class SignupView(TemplateView):
    template_name = 'signup.html'
    initial = {'key': 'value'}
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,email=email,password=password)

            args = username,email,password
            CreateUser.objects.create_student(*args)
            return HttpResponseRedirect('login')

        return render(request, self.template_name, {'form': form})
# def get(self, request, *args, **kwargs):
#     form = SignupForm()
#     return super(SignupView,self).get(request,signup_form=form)
    # def post(self,request, *args, **kwargs):
    #
    #     form = SignupForm(request.POST)
    #
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request,username=username,email=email,password=password)
    #
    #     return super(SignupView,self).get(request,signup_form=form)
# def signup(request):
#     if request.method == 'POST':#user has info and wants account now
#         if request.POST.get('password')==request.POST.get('confirm_password'):
#             try:
#                 user = User.objects.get(username=request.POST.get('username'))
#                 return render(request, 'signup.html',{'error':'User name is taken'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(request.POST.get('username'),password = request.POST.get('password'))
#                 auth.login(request,user)
#                 return redirect('home')
#         else:
#             return render(request, 'signup.html', {'form': SignupForm},{'error':'Passwords do not match'})
#     else:
#         form = SignupForm(request.POST)
#         user = form.save()
#         return render(request, 'signup.html', {'form': SignupForm})
class LoginView(TemplateView):
    template_name = 'login.html'
    initial = {'key': 'value'}
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self,request, *args, **kwargs):

        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request,email=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    messages.info(request,'Your account is inactive kindly '
                        'activate via the email we sent you')
            else:
                messages.info(request,'Your password or username is incorrect')
                return HttpResponseRedirect('/')

        return super(LoginView,self).get(request,login_form=form)




# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
#         if user is None:
#             auth.login(request,user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'form': LoginForm})
#
#     else:
#
#         form = LoginForm()
#         return render(request, 'login.html', {'form': LoginForm})
#
def account_logout(request):
    logout(request)
    url = reverse('students:login')
    return redirect(url,args=(),kwargs={})
