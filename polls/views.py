from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


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

def login(request):
    return render(request,'polls/login.html')

def register(request):
    return render(request,'polls/register.html')