from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Book
from .models import Author
from .models import Genre

main_menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title': 'Login', 'url_name': 'login'},
]


def index(request):
    book = Book.objects.all()
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {
        'book': book,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/index.html', context=context)


def about(request):
    context = {
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/about.html', context=context)


def feedback(request):
    context = {
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/feedback.html', context=context)


def login(request):
    return HttpResponse(
        '<h1>The ability to log in to your '
        'account and register will be added soon.</h1>'
    )


def show_books(request):
    book = Book.objects.all()
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {
        'books': book,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/show_books.html', context=context)


def specific_book(request, specific_id):
    books = Book.objects.filter(pk=specific_id)
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {
        'books': books,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/specific_book.html', context=context)


def show_authors(request):
    book = Book.objects.all()
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {
        'books': book,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/show_author.html', context=context)


def specific_author(request, specific_slug, ):
    books = Book.objects.all()
    author = Author.objects.filter(slug=specific_slug)
    genre = Genre.objects.all()
    context = {
        'books': books,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/specific_author.html', context=context)


def show_author_books(request, author_books_id, specific_slug):
    author = Author.objects.filter(slug=specific_slug)
    genre = Genre.objects.all()
    books = Book.objects.filter(author_id=author_books_id)
    context = {
        'books': books,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/show_author_books.html', context=context)


def show_genres(request):
    book = Book.objects.all()
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {
        'books': book,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
    }
    return render(request, 'appmy/show_genres.html', context=context)
