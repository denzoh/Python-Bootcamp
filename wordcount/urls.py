from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name = 'home'),
    path('eggs',views.eggs, name = 'eggs'),
    path('signup',views.signup, name = 'signup'),
    path('login',views.login,name = 'login')
    # path('login',views.login, name = 'login')
]
