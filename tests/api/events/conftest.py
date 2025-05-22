import pytest

from django.utils import timezone
from api.events.models import Event


@pytest.fixture
def event_factory(user_factory, city):
    def create_event(**kwargs):
        organizer = user_factory()
        defaults = {
            'title': 'Default Event',
            'about': 'Default description',
            'organizer': organizer,
            'city': city,
            'location': 'Default location',
            'start_time': timezone.now() + timezone.timedelta(days=1),
            'end_time': timezone.now() + timezone.timedelta(days=2),
        }
        defaults.update(kwargs)
        return Event.objects.create(**defaults)

    return create_event


@pytest.fixture
def event(event_factory):
    return event_factory()
