from django.urls import path, include
from . import views
from .views import (QuestionsHomeView)

urlpatterns = [
    path('view',QuestionsHomeView.as_view(), name="view_questions"),
    ]
