from rest_framework.exceptions import ValidationError
from .models import Event


def validate_attend_event(event: Event, user):
    if user == event.organizer:
        raise ValidationError("Organizer cannot be an attendee.")
    if user in event.attendees.all():
        raise ValidationError("You are already attending this event.")
    if event.capacity is not None and event.attendees.count() >= event.capacity:
        raise ValidationError("Event is at full capacity.")


def validate_unattend_event(event: Event, user):
    if user == event.organizer:
        raise ValidationError("Organizer cannot leave as attendee.")
    if user not in event.attendees.all():
        raise ValidationError("You are not attending this event.")
