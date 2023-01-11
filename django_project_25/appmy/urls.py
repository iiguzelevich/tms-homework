from django.urls import path

from .views import about
from .views import feedback
from .views import logout_user

from .views import Index
from .views import ShowBooks
from .views import ShowSpecificBook
from .views import ShowAuthors
from .views import ShowSpecificAuthor
from .views import ShowAuthorBooks
from .views import ShowGenres
from .views import ShowSpecificGenre
from .views import AddPost
from .views import RegisterUser
from .views import LoginUser

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(Index.as_view()), name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path(
        'books/', cache_page(60, cache='default_1')(ShowBooks.as_view()),
        name='show_books'
    ),    path(
        'books/<slug:specific_slug>/',
        ShowSpecificBook.as_view(),
        name='specific_book'
    ),
    path('authors/', ShowAuthors.as_view(), name='show_authors'),
    path(
        'author/<slug:author_slug>/',
        ShowSpecificAuthor.as_view(), name='specific_author'
    ),
    path(
        'author/<slug:author_slug>/<int:author_books_id>/',
        cache_page(60, cache='default')(ShowAuthorBooks.as_view()),
        name='show_author_books'
    ),
    path('genres/', ShowGenres.as_view(), name='show_genres'),
    path(
        'genres/<slug:genre_slug>/',
        ShowSpecificGenre.as_view(), name='specific_genre'
    ),
]
