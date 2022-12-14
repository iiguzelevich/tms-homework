from django.urls import path

from .views import about
from .views import feedback
from .views import login
from .views import show_books
from .views import specific_book
from .views import show_authors
from .views import specific_author
from .views import show_author_books
from .views import show_genres
from .views import specific_genre

from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('books/', show_books, name='show_books'),
    path('books/<slug:specific_slug>/', specific_book, name='specific_book'),
    path('authors/', show_authors, name='show_authors'),
    path(
        'author/<slug:author_slug>/',
        specific_author, name='specific_author'
    ),
    path(
        'author/<slug:author_slug>/<int:author_books_id>/',
        show_author_books, name='show_author_books'
    ),
    path('genres/', show_genres, name='show_genres'),
    path(
        'genres/<slug:genre_slug>/',
        specific_genre, name='specific_genre'
    ),
]
