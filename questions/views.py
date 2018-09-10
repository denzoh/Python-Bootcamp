from django.shortcuts import render
from django.views.generic import ListView
from .models import CreateQuestion
# Create your views here.
class QuestionsHomeView(ListView):
    template_name = 'questions_home.html'
    model = CreateQuestion
    context_object_name = 'questions'
    def get_context_data(self, **kwargs):
        context = super(QuestionsHomeView, self).get_context_data(**kwargs)
        return context
