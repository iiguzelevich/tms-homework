from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.views.generic import ListView

from .models import Book
from .models import Author
from .models import Genre

main_menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title': 'Login', 'url_name': 'login'},
]


class Index(ListView):
    model = Book
    template_name = 'appmy/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mainmenu'] = main_menu
        context['title'] = 'Main page'
        return context


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
        'title': 'Books',
    }
    return render(request, 'appmy/show_books.html', context=context)


def specific_book(request, specific_slug):
    book = Book.objects.get(slug=specific_slug)
    author = Author.objects.get(id=book.author_id)
    genre = Genre.objects.get(id=book.genre_id)
    context = {
        'book': book,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
        'title': f'Book: {book}',
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
        'title': 'Authors',
    }
    return render(request, 'appmy/show_author.html', context=context)


def specific_author(request, author_slug, ):
    author = Author.objects.get(slug=author_slug)
    books = Book.objects.all()
    genre = Genre.objects.all()
    context = {
        'genre': genre,
        'mainmenu': main_menu,
        'specific_author': author,
        'books': books,
        'title': f'Author: {author}',
    }
    return render(request, 'appmy/specific_author.html', context=context)


def show_author_books(request, author_books_id, author_slug):
    author = Author.objects.get(slug=author_slug)
    genre = Genre.objects.all()
    books = Book.objects.filter(author_id=author_books_id)
    context = {
        'books': books,
        'author': author,
        'genre': genre,
        'mainmenu': main_menu,
        'title': f'Books written by {author}',
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
        'title': 'Genres',

    }
    return render(request, 'appmy/show_genres.html', context=context)


def specific_genre(request, genre_slug):
    genre = Genre.objects.get(slug=genre_slug)
    books = Book.objects.all()
    context = {
        'books': books,
        'genre': genre,
        'mainmenu': main_menu,
        'title': f'Genre:{genre}',
    }
    return render(request, 'appmy/specific_genre.html', context=context)
