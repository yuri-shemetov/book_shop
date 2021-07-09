from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = ['pk', ]

class BookInCartAdmin(admin.ModelAdmin):
        list_display = ['pk', 'cart', 'quantity', 'unit_price', ]

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
