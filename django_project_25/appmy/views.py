from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Book
from .models import Author
from .models import Genre
from .models import Post

main_menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Feedback', 'url_name': 'feedback'},
    {'title': 'Login', 'url_name': 'login'},
]


class Index(ListView):
    paginate_by = 2
    model = Post
    template_name = 'appmy/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'Main page'
        return context


def about(request):
    context = {
        'main_menu': main_menu,
    }
    return render(request, 'appmy/about.html', context=context)


def feedback(request):
    context = {
        'main_menu': main_menu,
    }
    return render(request, 'appmy/feedback.html', context=context)


def login(request):
    return HttpResponse(
        '<h1>The ability to log in to your '
        'account and register will be added soon.</h1>'
    )


class ShowBooks(ListView):
    model = Book
    template_name = 'appmy/show_books.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Books'
        context['main_menu'] = main_menu
        return context


class ShowSpecificBook(DetailView):
    model = Book
    template_name = 'appmy/specific_book.html'
    slug_url_kwarg = 'specific_slug'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['book']
        context['main_menu'] = main_menu
        context['author'] = Author.objects.all()
        return context


class ShowAuthors(ListView):
    model = Author
    template_name = 'appmy/show_author.html'
    context_object_name = 'author'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'Authors'
        return context


class ShowSpecificAuthor(DetailView):
    model = Author
    context_object_name = 'specific_author'
    slug_url_kwarg = 'author_slug'
    template_name = 'appmy/specific_author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['books'] = Book.objects.all()
        return context


class ShowAuthorBooks(DetailView):
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'
    template_name = 'appmy/show_author_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['books'] = Book.objects.all()
        return context


class ShowGenres(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'appmy/show_genres.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        return context


class ShowSpecificGenre(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'appmy/specific_genre.html'
    slug_url_kwarg = 'genre_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['books'] = Book.objects.all()
        return context
