"""
This file contains models relevant to the flux application.
Specifically:
    class Ticket(models.Model):
        Defines ticket object, used to demand reviews on a specific subject.

    class Review(models.Model):
        Defines review object.

    class UserFollows(models.Model):
        Represents a "follow" relationship between two users.
        One user (the follower) subscribes to updates from another user.
"""
from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):
    """
    Defines ticket object, used to demand reviews on a specific subject.
    Attributes:
        title - CharField, max_length=128.
        description - TextField, max_length=2048, can be blank.
        author - ForeignKey to User object.
        image - ImageField, can be blank
        time_created - DateTimeField, added automatically.
        IMAGE_MAX_SIZE - defines max size for images to save space.

    Methods:
        def resize_image(self):
            resizes image in accordance with IMAGE_MAX_SIZE.
    """
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (400, 400)

    def resize_image(self):
        """Resizes image in accordance with IMAGE_MAX_SIZE."""
        if not self.image or not self.image.name:
            return
        try:
            img = Image.open(self.image)
            img.thumbnail(self.IMAGE_MAX_SIZE)
            img.save(self.image.path)
        except Exception as e:
            print(f"Image resizing failed: {e}")

    def save(self, *args, **kwargs):
        print("[Ticket model] save called")
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):
    """
    Serves to define Review type objects.
    Attributes:
        RATING_CHOICES - defines possible choices for rating.
        ticket - ForeignKey to Ticket object.
        rating - PositiveSmallIntegerField.
        headline - CharField.
        body - TextField.
        author - ForeignKey to User model.
        time_created - DateTimeField, added automatically.
    """
    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES
        )
    headline = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("Save model Review called")
        super().save(*args, **kwargs)


class UserFollows(models.Model):
    """
    Represents a "follow" relationship between two users.

    One user (the follower) subscribes to updates from another user.
    This model uses two foreign keys to represent the relationship:
    - `user`: the follower
    - `followed_user`: the user being followed
    """
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='follower')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed')
    class Meta:
        """
        Ensures that a user cannot follow the same user more than once
        by enforcing uniqueness on (user, followed_user) pairs.
        """
        unique_together = ('user', 'followed_user', )
