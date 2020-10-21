from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def home(request):
    choices = Question.CAT_CHOICES
    print(choices)
    return render(request, 'Exam/home.html', {'choices':choices})

def questions(request, choice):
    print(choice)
    ques = Question.objects.filter(catagory__exact=choice)
    return render(request, 'Exam/questions.html', {'ques': ques})
