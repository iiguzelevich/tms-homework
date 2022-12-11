from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from .forms import AddPostForm
from .forms import RegisterUserForm

from django.contrib.auth.views import LoginView

from django.contrib.auth import logout, login

from django.contrib.auth.forms import AuthenticationForm

from .models import Book
from .models import Author
from .models import Genre
from .models import Post

from .utils import DataMixin
from .utils import main_menu

from django.contrib.auth.mixins import LoginRequiredMixin


class Index(DataMixin, ListView):
    paginate_by = 2
    model = Post
    template_name = 'appmy/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Main page')
        context = dict(list(context.items()) + list(context_def.items()))
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


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'appmy/addpost.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Add your post')
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'appmy/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Registration')
        context = dict(list(context.items()) + list(context_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'appmy/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Login')
        context = dict(list(context.items()) + list(context_def.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ShowBooks(DataMixin, ListView):
    model = Book
    template_name = 'appmy/show_books.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Books')
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class ShowSpecificBook(DataMixin, DetailView):
    model = Book
    template_name = 'appmy/specific_book.html'
    slug_url_kwarg = 'specific_slug'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=context['book'])
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class ShowAuthors(DataMixin, ListView):
    model = Author
    template_name = 'appmy/show_author.html'
    context_object_name = 'author'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Authors')
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class ShowSpecificAuthor(DataMixin, DetailView):
    model = Author
    context_object_name = 'specific_author'
    slug_url_kwarg = 'author_slug'
    template_name = 'appmy/specific_author.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=context['specific_author'])
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class ShowAuthorBooks(DataMixin, DetailView):
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'
    template_name = 'appmy/show_author_books.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context_def = self.get_user_context(title=context['author'])
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class ShowGenres(DataMixin, ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'appmy/show_genres.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context_def = self.get_user_context(title='Genres')
        context = dict(list(context.items()) + list(context_def.items()))
        return context


class ShowSpecificGenre(DataMixin, DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'appmy/specific_genre.html'
    slug_url_kwarg = 'genre_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context_def = self.get_user_context(title=context['genre'])
        context = dict(list(context.items()) + list(context_def.items()))
        return context
