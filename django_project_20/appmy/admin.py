from django.contrib import admin
from .models import Book
from .models import Author
from .models import Genre


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title_book', 'book_description', 'year_publication', 'author',
    )
    search_fields = ('title_book', 'year_publication', 'author',)
    prepopulated_fields = {'slug': ('title_book',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'biography', 'photo',
    )
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    prepopulated_fields = {'slug': ('last_name',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
