from django import template
from flux.models import Review

register = template.Library()

@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag
def review_exists(ticket, user):
    return Review.objects.filter(ticket=ticket, author=user).exists()
