from django.db import models
from django.contrib.auth.models import User
from api.core.models import City


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='events'
    )
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='attendees'
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} attending {self.event.title}"
