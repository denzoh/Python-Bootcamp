from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'john doe'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'************'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'************'}))
    # class Meta:
    #     model = Createuser
    #     fields = ('username','email','password','confirm_password',)

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*************'}))
