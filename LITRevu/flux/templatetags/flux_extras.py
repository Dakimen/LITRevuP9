from django import template
from flux.models import Review
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag
def review_exists(ticket, user):
    return Review.objects.filter(ticket=ticket, author=user).exists()


@register.filter
def review_rating(score):
    score = int(score)
    stars_html = ''
    for i in range(5):
        if i < score:
            stars_html += '<i class="fa-solid fa-star fa-2xs"></i>'
        else:
            stars_html += '<i class="fa-regular fa-star fa-2xs"></i>'
    return mark_safe(stars_html)
