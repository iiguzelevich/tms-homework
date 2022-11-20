from django.urls import path

from .views import index
from .views import about
from .views import feedback
from .views import login
from .views import show_books
from .views import specific_book
from .views import show_authors
from .views import specific_author

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('books/', show_books, name='show_books'),
    path('books/<int:specific_id>/', specific_book, name='specific_book'),
    path('author/', show_authors, name='show_authors'),
    path(
        'author/<slug:specific_slug>/',
        specific_author, name='specific_author'
    ),

]
