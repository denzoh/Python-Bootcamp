from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name = 'home'),
    path('students/', include(('students.urls','students'),namespace=None)),
    path('questions/',include(('questions.urls','questions'),namespace=None))
    # path('lecturers/',include(('lecturers.urls','students'),namespace=None)),
]
