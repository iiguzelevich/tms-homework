from django.shortcuts import render
from django.http import HttpResponse

from .models import People
from .models import Profession

menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title': 'Login', 'url_name': 'login'},
]

category = [
    {'title': 'Professions', 'url_name': 'show_professions'},
    {'title': 'Interests', 'url_name': 'show_interests'},

]


def index(request):
    people = People.objects.all()
    profession = Profession.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'people': people,
        'profession': profession,
    }
    return render(request, 'appmy/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'category': category,
    }
    return render(request, 'appmy/about.html', context=context)


def feedback(request):
    context = {
        'menu': menu,
        'category': category,
    }
    return render(request, 'appmy/feedback.html',  context=context)


def show_professions(request):
    professions = Profession.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'professions': professions,
    }
    return render(request, 'appmy/show_professions.html', context=context)


def show_interests(request):
    context = {
        'menu': menu,
        'category': category,
    }
    return render(request, 'appmy/show_interests.html',  context=context)


def login(request):
    return HttpResponse('login')


def show_post(request):
    return HttpResponse(f'Show page')
