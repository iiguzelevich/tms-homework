from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import Http404

from .models import People
from .models import Category

menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Add information', 'url_name': 'add_information'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title': 'Login', 'url_name': 'login'},
]


def index(requsest):
    posts = People.objects.all()
    category = Category.objects.all()
    context = {
        'posts': posts,
        'category': category,
        'title': 'Main page',
        'menu': menu,
        'category_selected': 0,
    }
    return render(requsest, 'people/index.html', context=context)


def about(requsest):
    return render(requsest, 'people/about.html',
                  {'menu': menu, 'title': 'about my site'}
                  )


def add_information(requsest):
    return render(requsest, 'people/add_information.html',
                  {'menu': menu, 'title': 'add information'}
                  )


def login(requsest):
    return HttpResponse('login')


def feedback(requsest):
    return HttpResponse('feddback')


def show_post(requsest, post_id):
    return HttpResponse(f'Show page with id {post_id}')


def show_category(requsest, category_id):
    posts = People.objects.filter(category_id=category_id)
    category = Category.objects.all()
    context = {
        'posts': posts,
        'category': category,
        'title': 'no Main page',
        'menu': menu,
        'category_selected': category_id,
    }
    return render(requsest, 'people/index.html', context=context)


def pageNotFound(requset, exception):
    return HttpResponseNotFound(f'<h1> Page not found</h1>')
