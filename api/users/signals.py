from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from api.users.services import ProfileService


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileService.create_profile(instance)
