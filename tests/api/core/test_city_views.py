import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_city_list(api_client, city_factory):
    city1 = city_factory(name="city1")
    city2 = city_factory(name="city2")

    url = reverse("city-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    cities = (city["name"] for city in response.data["results"])

    assert city1.name in cities
    assert city2.name in cities


@pytest.mark.django_db
def test_city_detail(auth_client, city):
    url = reverse("city-detail", kwargs={"pk": city.pk})
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert "name" in response.data
    assert "country" in response.data
