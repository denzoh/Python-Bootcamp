from django.urls import path, include
from . import views
from .views import (SignupView,LoginView)

urlpatterns = [
    #path('',LoginView.as_view(), name="login"),
    path('login',LoginView.as_view(),name = 'login'),
    path('signup',SignupView.as_view(), name = 'signup'),
    path('logout',views.account_logout, name='logout')
    ]
