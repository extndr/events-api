import pytest
from django.utils import timezone
from django.urls import reverse

from api.events.serializers import EventSerializer, EventSummarySerializer


@pytest.mark.django_db
def test_event_serializer_input_valid(user, city):
    data = {
        'title': 'Event Title',
        'about': 'Some description',
        'city': city.id,
        'location': 'Somewhere',
        'start_time': timezone.now() + timezone.timedelta(days=1),
        'end_time': timezone.now() + timezone.timedelta(days=2)
    }

    serializer = EventSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

    event = serializer.save(organizer=user)

    assert event.title == data['title']
    assert event.organizer == user
    assert event.city == city


@pytest.mark.django_db
def test_event_serializer_invalid_missing_fields():
    data = {
        'about': '',
        'city': '',
        'location': '',
        'start_time': '',
        'end_time': '',
    }

    serializer = EventSerializer(data=data)

    assert not serializer.is_valid()

    for field in data:
        assert field in serializer.errors


@pytest.mark.django_db
def test_event_serializer_input_invalid_end_before_start(city):
    data = {
        'title': 'Invalid Timing Event',
        'about': 'End time is before start time',
        'city': city.id,
        'location': 'Somewhere',
        'start_time': timezone.now() + timezone.timedelta(days=2),
        'end_time': timezone.now() + timezone.timedelta(days=1)
    }

    serializer = EventSerializer(data=data)

    assert not serializer.is_valid()
    assert 'end_time' in serializer.errors


@pytest.mark.django_db
def test_event_serializer_input_invalid_start_in_the_past(city):
    data = {
        'title': 'Event in the Past',
        'about': 'This event starts in the past.',
        'city': city.id,
        'location': 'Somewhere',
        'start_time': timezone.now() - timezone.timedelta(days=1),
        'end_time': timezone.now()
    }

    serializer = EventSerializer(data=data)

    assert not serializer.is_valid()
    assert 'start_time' in serializer.errors


@pytest.mark.django_db
def test_event_serializer_output(user, city, factory, event):
    url = reverse('event-detail', kwargs={'pk': event.pk})
    request = factory.get(url)
    context = {'request': request}

    serializer = EventSerializer(event, context=context)
    data = serializer.data

    assert data['title'] == event.title
    assert data['about'] == event.about
    assert data['city'] == city.name
    assert data['location'] == event.location
    assert data['organizer']['username'] == event.organizer.username
    assert data['attendees_count'] == 0


@pytest.mark.django_db
def test_event_summary_serializer_output(factory, event):
    url = reverse('event-list')
    request = factory.get(url)
    context = {'request': request}

    serializer = EventSummarySerializer(event, context=context)
    data = serializer.data

    assert 'title' in data
    assert 'city' in data
    assert 'start_time' in data
    assert 'attendees_count' in data
    assert 'url' in data
