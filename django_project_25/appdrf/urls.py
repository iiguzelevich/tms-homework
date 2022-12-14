from django.urls import path
from .views import BooksList
from .views import AuthorsList
from .views import GenresList
from .views import GenreDetail

urlpatterns = [
    path('api/bookslist/', BooksList.as_view()),
    path('api/authorslist/', AuthorsList.as_view()),
    path('api/generslist/', GenresList.as_view()),
    path('api/generdetail/<int:pk>/', GenreDetail.as_view()),

]
