from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_three_questions = get_list_or_404(Question.objects.order_by('pub_date'))
    return render(request, 'polls/index.html', {'latest_question_list' : latest_three_questions,})


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select any choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result',args=(question_id,)))


def detail(request, question_id):
    question = get_object_or_404( Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def result(request, question_id):
    return render(request, 'polls/result.html', {'question':Question.objects.get(pk=question_id)})
