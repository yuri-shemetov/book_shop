from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display=[
    'name', 
    'genre',
    'seria',
    'pages',
    'publisher',
    ]

admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Promo)
