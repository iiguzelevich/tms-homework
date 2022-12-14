from .serializers import BookSerializer
from .serializers import AuthorsSerializer
from .serializers import GenreSerializer

from appmy.models import Book
from appmy.models import Author
from appmy.models import Genre

from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorsList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer


class GenresList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
