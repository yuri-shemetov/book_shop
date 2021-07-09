from django import template
from .. import models
from django.contrib.contenttypes.models import ContentType


register = template.Library()

@register.inclusion_tag('comments/show_comments_book.html',takes_context=True)
def show_comments_book(context):
    obj = context.get('object')
    content_type = ContentType.objects.get_for_model(obj)
    content_type_id = content_type.pk
    comments = models.Comment.objects.filter(content_type=content_type, object_id=obj.pk)
    next_step = context.get('request').path
    comments = list(reversed(comments))
    
    return {
        'comments': comments, 
        'next_step': next_step, 
        'content_type_id': content_type_id, 
        'object_id': obj.pk
    }