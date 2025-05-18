from django.db import models
from django.contrib.auth.models import AbstractUser

from api.core.models import Country, City


class User(AbstractUser):
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
