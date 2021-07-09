from django.db import models
from django.urls import reverse

class Series(models.Model):
    series = models.CharField(
        max_length=30,
        verbose_name="Серия книги"
    )
    def __str__(self) -> str:
        return f"Серия - {self.series}"

    def get_absolute_url(self):
        return reverse('series')

    class Meta:
        verbose_name = "Серию"
        verbose_name_plural = "Серии"

class Publisher(models.Model):    
    name = models.CharField(
        max_length=25,
        verbose_name="Название издательства"
    )
    city = models.CharField(
        max_length=25,
        verbose_name="Город издания"
    )
    def __str__(self) -> str:
        return f"Издательство: {self.name}, {self.city}"

    def get_absolute_url(self):
        return reverse ('publishers')

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

class Author(models.Model):
    number = models.IntegerField(
        
        verbose_name="Количество авторов",
    )
    name = models.CharField(
        max_length=30,
        verbose_name="Автор(ы)"
    )
    created = models.DateTimeField(
        verbose_name="Дата внесения в БД",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Дата последнего редактирования",
        auto_now=True,
        auto_now_add=False
    )
    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('authors')

    class Meta:
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"
    

class Genre(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Название жанра"
    )
    description = models.TextField(
        verbose_name="Описание жанра",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse ('genres')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

