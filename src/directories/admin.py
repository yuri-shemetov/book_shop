from django.contrib import admin
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display=['pk', 
    'number',
    'name', 
    'created',
    'updated'
    ]
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)
admin.site.register(models.Series)
