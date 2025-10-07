"""
This file is used to store and access models,
relating to user authentication.

Contains the User model that inherits directly from Abstract User.
Used in this application as the user model.
"""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model directly inheriting from AbstractUser, no custom changes.
    """
    pass
