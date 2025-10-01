from django import template
from flux.models import UserFollows

register = template.Library()

@register.filter
def is_following(user, target_user):
    return UserFollows.objects.filter(user=user, followed_user=target_user).exists()
