from .serializers import BookSerializer
from .serializers import AuthorsSerializer
from .serializers import GenreSerializer
from .serializers import PostSerializer

from appmy.models import Book
from appmy.models import Author
from appmy.models import Genre
from appmy.models import Post

from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from rest_framework.viewsets import ModelViewSet

from rest_framework import filters

from .paginations import StandardPagination
from .paginations import BasePagination


class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title_book', 'year_publication', 'genre']
    search_fields = ['author__last_name']
    pagination_class = StandardPagination


class AuthorsList(ListAPIView):
    queryset = Author.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    serializer_class = AuthorsSerializer
    pagination_class = StandardPagination


class AuthorDetail(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer


class GenresList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'id']
    search_fields = ['name', 'id']
    pagination_class = BasePagination


class GenreDetail(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ['post_book__title_book']
    pagination_class = StandardPagination
