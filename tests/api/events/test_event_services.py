import pytest
from rest_framework.exceptions import ValidationError
from api.events.services import EventService


@pytest.mark.django_db
def test_add_attendee(user, event):
    result = EventService.add_attendee(event, user)

    assert 'now attending' in result
    assert user in event.attendees.all()


@pytest.mark.django_db
def test_add_organizer_as_attendee(user, event_factory):
    event = event_factory(organizer=user)

    with pytest.raises(ValidationError):
        EventService.add_attendee(event, user)


@pytest.mark.django_db
def test_add_attendee_already_attending(user, event):
    event.attendees.add(user)

    with pytest.raises(ValidationError):
        EventService.add_attendee(event, user)


@pytest.mark.django_db
def test_add_attendee_event_full(user_factory, event_factory):
    user1 = user_factory(username='user1')
    user2 = user_factory(username='user2')

    event = event_factory(capacity=1)
    event.attendees.add(user1)

    with pytest.raises(ValidationError):
        EventService.add_attendee(event, user2)


@pytest.mark.django_db
def test_remove_attendee(user, event):
    event.attendees.add(user)

    result = EventService.remove_attendee(event, user)

    assert result == "You have successfully left the event."
    assert user not in event.attendees.all()


@pytest.mark.django_db
def test_remove_attendee_as_organizer(user, event_factory):
    event = event_factory(organizer=user)
    event.attendees.add(user)

    with pytest.raises(ValidationError):
        EventService.remove_attendee(event, user)


@pytest.mark.django_db
def test_remove_attendee_not_in_list(user, event):
    with pytest.raises(ValidationError):
        EventService.remove_attendee(event, user)
