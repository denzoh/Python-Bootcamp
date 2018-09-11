from django.urls import path, include
from . import views
from .views import (SignupView,LoginView,LogOutView)

urlpatterns = [
    path('login',LoginView.as_view(),name = 'login'),
    path('signup',SignupView.as_view(), name = 'signup'),
    path('logout',LogOutView.as_view(), name='logout')
    ]
