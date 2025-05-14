from .models import Event
from .validators import validate_attend_event, validate_unattend_event


class AttendeeService:
    @staticmethod
    def attend_event(event: Event, user) -> str:
        validate_attend_event(event, user)
        event.attendees.add(user)
        return "You are now attending the event."

    @staticmethod
    def unattend_event(event: Event, user) -> str:
        validate_unattend_event(event, user)
        event.attendees.remove(user)
        return "You have successfully left the event."
