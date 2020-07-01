from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, User


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

def registration(request):
    return render(request,'polls/registration.html')

def loginPage(request):
    return render(request,'polls/login.html')

def register(request):
    email = request.POST['email']
    psw = request.POST['psw']
    psw_repeat = request.POST['psw-repeat']

    if( psw != psw_repeat ):
        return HttpResponseRedirect(reverse('polls:registration'))
    
    if( User.objects.filter(email=email).count()>0 ):
        return HttpResponseRedirect(reverse('polls:loginPage'))
    
    else:
        User.objects.create(email=email,password=psw)
        return HttpResponseRedirect(reverse('polls:loginPage'))

def login(request):
    email = request.POST['email']
    psw = request.POST['psw']
    if( User.objects.filter(email=email,password=psw).count()==1 ):
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return HttpResponseRedirect(reverse('polls:loginPage'))