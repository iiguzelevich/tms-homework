from django.db import models


class People(models.Model):
    class Meta:
        verbose_name = u'Person'
        verbose_name_plural = u'People'

    first_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name=u'Name'
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name=u'Surname'
    )
    birthday = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=u'Birthday'
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name=u'Photo',
    )

    people_profession = models.ForeignKey(
        'Profession',
        verbose_name=u'Profession',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    article = models.TextField(
        blank=True,
        verbose_name=u'Article'
    )

    time_create = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profession(models.Model):
    class Meta:
        verbose_name = u'Profession'
        verbose_name_plural = u'Professions'

    profession_title = models.CharField(
        max_length=200,
        blank=True,
    )

    position = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.profession_title
