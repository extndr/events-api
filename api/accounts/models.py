from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

from api.core.models import Country, City


class User(AbstractUser):
    username = models.CharField(
        max_length=150, unique=True, validators=[MinLengthValidator(3)]
    )
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
