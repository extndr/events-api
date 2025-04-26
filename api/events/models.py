from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=24, unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='cities'
    )

    def __str__(self):
        return self.name
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, related_name='events'
    )
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='organized_events'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
