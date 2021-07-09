from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='carts',
        verbose_name='Cart',
        on_delete=models.PROTECT
        )

    @property
    def total_price(self):
        books = self.books.all()
        total_price = 0
        for book in books:
            total_price += book.unit_price*book.quantity
        return total_price

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Cart',
        related_name='books'
    )
    book = models.ForeignKey(
        'shop.Book',
        on_delete=models.PROTECT,
        verbose_name='Book',
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1,
    )
    unit_price = models.DecimalField(
        verbose_name='Unit price',
        max_digits=5,
        decimal_places=2,
    )

    @property
    def total_price(self):
        return self.unit_price * self.quantity