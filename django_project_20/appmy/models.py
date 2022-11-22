from django.db import models
from django.urls import reverse


class Book(models.Model):
    class Meta:
        verbose_name = u'Book'
        verbose_name_plural = u'Books'

    title_book = models.CharField(
        max_length=300,
        blank=False,
        verbose_name='Title of the book'
    )

    genre = models.ForeignKey(
        'Genre',
        verbose_name='Genre',
        on_delete=models.PROTECT,
    )

    author = models.ForeignKey(
        'Author',
        verbose_name='Author of the book',
        on_delete=models.PROTECT,
    )

    book_description = models.TextField(
        blank=True,
        verbose_name='Book description',
    )

    year_publication = models.CharField(
        max_length=4,
        blank=True,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.title_book

    def get_absolute_url(self):
        return reverse('specific_book', kwargs={'specific_id': self.pk})


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name="author's name",
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="author's surname",
    )
    biography = models.TextField(
        verbose_name='Biography',
        blank=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('specific_author', kwargs={'specific_slug': self.slug})

    def get_url_show_author_books(self):
        return reverse(
            'show_author_books',
            kwargs={
                'author_books_id': self.id,
                'specific_slug': self.slug
            }
        )


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Genre of the book'
    )

    def __str__(self):
        return self.name
