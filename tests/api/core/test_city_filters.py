import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_city_filter_by_country(api_client, city):
    url = reverse('city-list')
    response = api_client.get(url, {'country': city.country.code})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['name'] == city.name
    assert response.data['results'][0]['country'] == city.country.name
