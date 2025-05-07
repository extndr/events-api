from django.db import models
from django.contrib.auth.models import User
from api.core.models import City


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='events'
    )
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='organized_events'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title
