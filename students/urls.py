from django.urls import path, include
from . import views

urlpatterns = [
    #path('',LoginView.as_view(), name="login"),
    path('login',views.login,name = 'login'),
    path('signup',views.signup, name = 'signup'),
    path('logout',views.account_logout, name='logout')
    ]
