from directories.models import Author, Genre, Publisher, Series
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

class Book(models.Model):
    picture = models.ImageField(
        "Картинка",
        upload_to='books/%Y/%m/%d',
    )
    
    name = models.CharField(
        max_length=40,
        verbose_name='Название книги',
    )

    price = models.FloatField(
        verbose_name='Цена',
    )

    author = models.ManyToManyField(
        Author,
        related_name='Автор',
        verbose_name='Автор',
    )

    seria = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        related_name='Серия',
        verbose_name="Серия",
    )

    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='Жанр',
        verbose_name="Жанр",
    )

    year = models.IntegerField(
        verbose_name='Год издания',
    )

    pages = models.IntegerField(
        verbose_name='Страниц',
    )

    binding = models.CharField(
        verbose_name='Переплет',
        max_length=30,
    )

    form = models.CharField(
        verbose_name='Формат',
        max_length=30,
    )

    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=30,
    )

    weight = models.IntegerField(
        verbose_name='Вес',
    )

    age = models.IntegerField(
        verbose_name="Возрастные ограничения",
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name="Издательство",
        verbose_name="Издательство",
    )

    quantity = models.IntegerField(
        verbose_name='Количество книг',
    )

    avtive = models.BooleanField(
        verbose_name='Активный',
        default=False,
    )

    rating = models.FloatField(
        verbose_name='Рейтинг',
    )

    comments = GenericRelation(Comment)

    created = models.DateTimeField(
        verbose_name="Дата внесения",
        auto_now=False,
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name="Дата последнего редактирования",
        auto_now=True,
        auto_now_add=False,
    )

    def __str__(self) -> str:
        return f'"{self.name}" - {self.author.all()[0]}'

    def get_absolute_url(self):
        return reverse ('books-managers')

    class Meta:
        verbose_name="Книга"
        verbose_name_plural="Книги"

class Promo(models.Model):
    picture = models.ImageField(
        "Акции",
        upload_to='promo/%Y/%m/%d',
    )
    name = models.CharField(
        max_length=40,
        verbose_name='Название акции',
    )
    description = models.TextField(
        verbose_name="Подробнее об акции",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'Акция: {self.name}'

    def get_absolute_url(self):
        return reverse ('promo')

    class Meta:
        verbose_name="Акция"
        verbose_name_plural="Акции"