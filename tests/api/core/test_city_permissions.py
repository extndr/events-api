import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_city_creation_forbidden_for_regular_user(client, country):
    url = reverse("city-list")
    response = client.post(url, {"name": "City2", "country": country.id})

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_city_creation_allowed_for_admin_user(admin_client, country):
    url = reverse("city-list")
    response = admin_client.post(url, {"name": "City2", "country": country.id})

    assert response.status_code == status.HTTP_201_CREATED
