from rest_framework.exceptions import ValidationError

from .models import Event


class EventService:
    """
    Service class to handle event logic, such as adding and removing attendees.
    """

    @staticmethod
    def add_attendee(event: Event, user) -> str:
        """
        Add a user to the event's attendees list.
        """

        if user == event.organizer:
            raise ValidationError("Organizer cannot be an attendee.")
        if user in event.attendees.all():
            raise ValidationError("You are already attending this event.")
        if event.capacity is not None and event.attendees.count() >= event.capacity:
            raise ValidationError("Event is at full capacity.")

        event.attendees.add(user)
        return "You are now attending the event."

    @staticmethod
    def remove_attendee(event: Event, user) -> str:
        """
        Remove a user from the event's attendees list.
        """

        if user == event.organizer:
            raise ValidationError("Organizer cannot leave as attendee.")
        if user not in event.attendees.all():
            raise ValidationError("You are not attending this event.")

        event.attendees.remove(user)
        return "You have successfully left the event."
