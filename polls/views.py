from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_three_questions = get_list_or_404(Question.objects.order_by('pub_date')[:3])
    return render(request, 'polls/index.html', {'latest_question_list' : latest_three_questions,})


def vote(request, question_id):
    return HttpResponse(f'You are voting on question "{question_id}"')


def detail(request, question_id):
    question = get_object_or_404( Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def result(request, question_id):
    return HttpResponse(f'You are looking at result of "{question_id}"')
