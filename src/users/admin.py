from django.contrib import admin
from . import models
class UserDetailAdmin(admin.ModelAdmin):
    list_display=[
    'pk',
    'username',
    ]
admin.site.register(models.UserDetail, UserDetailAdmin)