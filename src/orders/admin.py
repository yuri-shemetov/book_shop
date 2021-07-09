from django.contrib import admin
from . import models

class OrderAdmin(admin.ModelAdmin):
        list_display = ['pk', 'cart', 'status', 'login', 'phone_number', 'first_name', 'last_name', 'created', 'updated']
class StatusAdmin(admin.ModelAdmin):
        list_display = ['pk', 'name']

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Status, StatusAdmin)


