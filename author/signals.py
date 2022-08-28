from django.http import request
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Author
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def post_save_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
