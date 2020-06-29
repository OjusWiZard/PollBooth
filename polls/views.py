from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World, views.py")


def vote(request, question_id):
    return HttpResponse(f'You are voting on question "{question_id}"')


def detail(request, question_id):
    return HttpResponse(f'You are looking at "{question_id}"')


def result(request, question_id):
    return HttpResponse(f'You are looking at result of "{question_id}"')
