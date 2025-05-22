import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_country_creation_forbidden_for_regular_user(auth_client):
    url = reverse('country-list')
    response = auth_client.post(url, {'name': 'Country2'})

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_country_creation_allowed_for_admin_user(admin_client):
    url = reverse('country-list')
    response = admin_client.post(url, {'name': 'Country2'})

    assert response.status_code == status.HTTP_201_CREATED
