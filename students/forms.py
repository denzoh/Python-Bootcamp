from django import forms
from django.forms import ModelForm
from .models import CreateUser

class SignupForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'john doe'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'************'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'************'}))
    class Meta:
        model = CreateUser
        fields = ('username','email','password','confirm_password',)

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*************'}))
