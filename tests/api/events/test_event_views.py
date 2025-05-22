import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_event_list(api_client, event_factory):
    event1 = event_factory(title='event1')
    event2 = event_factory(title='event2')

    url = reverse('event-list')
    response = api_client.get(url)

    assert response.status_code == 200

    events = (event['title'] for event in response.data['results'])

    assert event1.title in events
    assert event2.title in events


@pytest.mark.django_db
def test_event_detail(auth_client, event):
    url = reverse('event-detail', kwargs={'pk': event.pk})
    response = auth_client.get(url)
    data = response.data

    assert response.status_code == 200

    assert 'title' in data
    assert 'about' in data
    assert 'city' in data
    assert 'location' in data
    assert 'organizer' in data
    assert 'attendees_count' in data


@pytest.mark.django_db
def test_event_update(auth_client, user, event_factory):
    event = event_factory(organizer=user)

    url = reverse('event-detail', kwargs={'pk': event.pk})
    response = auth_client.patch(url, {'about': 'Updated info'})

    assert response.status_code == status.HTTP_200_OK

    event.refresh_from_db()

    assert response.data['about'] == 'Updated info'


@pytest.mark.django_db
def test_attend_event(auth_client, event, user):
    url = reverse('event-attend', kwargs={'pk': event.pk})
    response = auth_client.post(url)

    assert response.status_code == status.HTTP_200_OK
    assert user in event.attendees.all()


@pytest.mark.django_db
def test_unattend_event(auth_client, event, user):
    event.attendees.add(user)

    url = reverse('event-unattend', kwargs={'pk': event.pk})
    response = auth_client.post(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert user not in event.attendees.all()
