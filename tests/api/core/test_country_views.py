import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_country_list(api_client, country_factory):
    country1 = country_factory(name='country1')
    country2 = country_factory(name='country2')

    url = reverse('country-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    countries = (country['name'] for country in response.data['results'])

    assert country1.name in countries
    assert country2.name in countries


@pytest.mark.django_db
def test_country_detail(auth_client, country):
    url = reverse('country-detail', kwargs={'pk': country.pk})
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert 'name' in response.data
