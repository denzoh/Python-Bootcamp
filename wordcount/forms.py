from django import forms

class SignupForm(forms.Form):
    #name = forms.CharField(widget=forms.NameInput(attrs={'placeholder':'enter name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'************'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'************'}))

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*************'}))
