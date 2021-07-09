from orders import models

from django import template

register = template.Library()

@register.simple_tag
def new_order():
    orders = models.Order.objects.values('status')
    quantity = 0
    for status in orders:
        for key, value in status.items():
            if value == 1:
                quantity += 1
    if quantity == 0:
        quantity=''
    else:
        quantity = str(quantity) + '+'
    return quantity