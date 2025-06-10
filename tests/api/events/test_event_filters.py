import pytest
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from datetime import timedelta


@pytest.mark.django_db
def test_filter_by_start_time(api_client, event_factory):
    event1 = event_factory(start_time=timezone.now() + timedelta(days=1))
    event2 = event_factory(start_time=timezone.now() + timedelta(days=5))

    url = reverse('event-list')
    response = api_client.get(url, {'start_time': (timezone.now() + timedelta(days=2)).isoformat()})

    assert response.status_code == status.HTTP_200_OK
    ids = [e['id'] for e in response.data['results']]
    assert event2.id in ids
    assert event1.id not in ids


@pytest.mark.django_db
def test_filter_by_end_time(api_client, event_factory):
    event1 = event_factory(end_time=timezone.now() + timedelta(hours=2))
    event2 = event_factory(end_time=timezone.now() + timedelta(hours=10))

    url = reverse('event-list')
    response = api_client.get(url, {'end_time': (timezone.now() + timedelta(hours=3)).isoformat()})

    assert response.status_code == status.HTTP_200_OK
    ids = [e['id'] for e in response.data['results']]
    assert event1.id in ids
    assert event2.id not in ids


@pytest.mark.django_db
def test_filter_by_organizer(api_client, user_factory, event_factory):
    organizer1 = user_factory(username='alice')
    organizer2 = user_factory(username='bob')
    event1 = event_factory(organizer=organizer1)
    event_factory(organizer=organizer2)

    url = reverse('event-list')
    response = api_client.get(url, {'organizer': 'alice'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['id'] == event1.id


@pytest.mark.django_db
def test_filter_by_city(api_client, city_factory, event_factory):
    city1 = city_factory(name='London')
    city2 = city_factory(name='Paris')
    event1 = event_factory(city=city1)
    event_factory(city=city2)

    url = reverse('event-list')
    response = api_client.get(url, {'city': 'London'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['id'] == event1.id


@pytest.mark.django_db
def test_filter_by_country(api_client, country_factory, city_factory, event_factory):
    country = country_factory(name='Country 1', country_code='UK')
    city = city_factory(name='City 1', country=country)
    event = event_factory(city=city)

    url = reverse('event-list')
    response = api_client.get(url, {'country': country.code})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['id'] == event.id
