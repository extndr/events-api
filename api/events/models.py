from django.db import models
from django.contrib.auth.models import User
from api.core.models import City


class Event(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
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
    attendees = models.ManyToManyField(
        User,
        related_name='events_attending',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('start_time',)
