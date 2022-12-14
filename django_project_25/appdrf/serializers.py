from rest_framework.serializers import ModelSerializer
from appmy.models import Book
from appmy.models import Author
from appmy.models import Genre


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title_book', 'author', 'genre', 'year_publication', ]


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'id']
