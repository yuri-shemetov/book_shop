from comments.models import Comment
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

class Status(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="Статус"
    )
    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name="Статус"
        verbose_name_plural="Статусы"

class Order(models.Model):
    cart = models.ForeignKey(
        'carts.Cart',
        on_delete=models.PROTECT,
        verbose_name='Order',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='Status',
    )
    login = models.CharField(
        max_length=15,
        verbose_name='Login',
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Phone',
    )
    first_name = models.CharField(
        max_length=15,
        verbose_name='First name',
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Last name',
    )
    comments = GenericRelation(Comment)
    
    created = models.DateTimeField(
        verbose_name='Created',
        auto_now = False,
        auto_now_add = True,
    )
    updated = models.DateTimeField(
        verbose_name='Update',
        auto_now = True,
        auto_now_add = False,
    )
    class Meta:
        verbose_name="Заказ"
        verbose_name_plural="Заказы"

    def __str__(self) -> str:
        return f'"{self.cart}"'