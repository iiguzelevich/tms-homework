from django.contrib import admin
from .models import Book
from .models import Author
from .models import Genre
from .models import Post

from django.utils.safestring import mark_safe


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title_book', 'book_description', 'year_publication', 'author',
    )
    search_fields = ('title_book', 'year_publication', 'author',)
    prepopulated_fields = {'slug': ('title_book',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'biography', 'get_html_photo',
    )
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    prepopulated_fields = {'slug': ('last_name',)}

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50>')

    get_html_photo.short_description = 'photo'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'information', 'post_book', 'creator',
        'time_create', 'time_update',
    )
    search_fields = (
        'information', 'post_book', 'creator', 'time_create', 'time_update',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Post, PostAdmin)
