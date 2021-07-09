from django import template
from .. import models
from django.contrib.contenttypes.models import ContentType
from orders import models as models_order

register = template.Library()

@register.inclusion_tag('comments/show_comments.html',takes_context=True)
def show_comments(context):
    obj = '"' + str(context.get('object')) + '"'
    
    orders = models_order.Order.objects.all()
    
    for order in orders:
        if str(order) == obj:
            obj_order = order
    
    content_type = ContentType.objects.get_for_model(obj_order)
    content_type_id = content_type.pk
    comments = models.Comment.objects.filter(content_type=content_type, object_id=obj_order.pk)
    next_step = str(context.get('request').path) + "?filter=" + str(obj_order.pk)
    comments = list(reversed(comments))
    
    return {
        'comments': comments, 
        'next_step': next_step, 
        'content_type_id': content_type_id, 
        'object_id': obj_order.pk
    }