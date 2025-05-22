import pytest
from django.urls import reverse
from rest_framework import status
from django.utils import timezone


@pytest.mark.django_db
def test_event_creation_forbidden_for_unauthenticated_user(api_client, city):
    url = reverse('event-list')
    data = {
        'title': 'Test Event',
        'about': 'Test Event Description',
        'city': city.id,
        'location': 'Test Location',
        'start_time': timezone.now() + timezone.timedelta(days=1),
        'end_time': timezone.now() + timezone.timedelta(days=2),
    }

    # Unauthenticated user should not be able to create an event
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_event_creation_allowed_for_authenticated_user(auth_client, city):
    url = reverse('event-list')
    data = {
        'title': 'Test Event',
        'about': 'Test Event Description',
        'city': city.id,
        'location': 'Test Location',
        'start_time': timezone.now() + timezone.timedelta(days=1),
        'end_time': timezone.now() + timezone.timedelta(days=2),
    }

    # Authenticated user should be able to create an event
    response = auth_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_event_update_allowed_for_organizer(auth_client, user, event_factory):
    event = event_factory(organizer=user)

    url = reverse('event-detail', kwargs={'pk': event.pk})
    data = {'about': 'Updated Event Info'}

    # Organizer should be able to update the event
    response = auth_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    event.refresh_from_db()
    assert event.about == 'Updated Event Info'


@pytest.mark.django_db
def test_event_update_forbidden_for_non_organizer(auth_client, user_factory, event_factory):
    user = user_factory()  # Organizer user
    other_user = user_factory()  # Non-organizer user
    event = event_factory(organizer=user)

    url = reverse('event-detail', kwargs={'pk': event.pk})
    data = {'about': 'Updated Event Info'}

    # Non-organizer should not be able to update the event
    auth_client.force_authenticate(user=other_user)
    response = auth_client.patch(url, data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_event_detail_read_allowed_for_authenticated_user(auth_client, event):
    url = reverse('event-detail', kwargs={'pk': event.pk})

    # Any authenticated user should be able to read event details
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == event.title


@pytest.mark.django_db
def test_event_detail_read_allowed_for_unauthenticated_user(api_client, event):
    url = reverse('event-detail', kwargs={'pk': event.pk})

    # Unauthenticated user should be able to read event details
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == event.title
