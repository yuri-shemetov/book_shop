from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserDetail(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер мобильного телефона',
    )

    country = models.CharField(
        verbose_name='Страна',
        max_length=15,
        blank=True,
        null=True,
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=20,
        blank=True,
        null=True,
    )

    index = models.IntegerField(
        verbose_name='Индекс',
        blank=True,
        null=True,
    )

    address_1 = models.CharField(
        verbose_name='Адрес 1',
        max_length=40,
        blank=True,
        null=True,
    )

    address_2 = models.CharField(
        verbose_name='Адрес 2',
        max_length=40,
        blank=True,
        null=True,
    )

    info = models.CharField(
        verbose_name='Дополнительная информация',
        max_length=80,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.username}'

    def get_absolute_url(self):
        return reverse ('users:user-detail')

    class Meta:
        verbose_name="Подробности о пользователе"
        verbose_name_plural="Подробнее о пользователях"