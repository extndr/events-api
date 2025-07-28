import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_is_self_or_read_only_permission_for_self(auth_client, user):
    url = reverse("user-detail", kwargs={"pk": user.pk})
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    response = auth_client.put(url, {"username": "newusername"})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_is_self_or_read_only_permission_for_other_user(api_client, user_factory):
    user1 = user_factory(username="user1")
    user2 = user_factory(username="user2")

    api_client.force_authenticate(user=user1)

    url = reverse("user-detail", kwargs={"pk": user2.pk})
    response = api_client.put(url, {"username": "hacked_username"})

    assert response.status_code == 403  # Forbidden
