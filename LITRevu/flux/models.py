from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (400, 400)
    def resize_image(self):
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
        super().save()


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='followed_by')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='following')
    class Meta:
        unique_together = ('user', 'followed_user', )
