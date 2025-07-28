import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_user_list_view(api_client, user_factory):
    user1 = user_factory(username="testuser1")
    user2 = user_factory(username="testuser2")

    response = api_client.get(reverse("user-list"))

    assert response.status_code == status.HTTP_200_OK

    users = (user["username"] for user in response.data["results"])

    assert user1.username in users
    assert user2.username in users


@pytest.mark.django_db
def test_user_detail_view(auth_client, user):
    url = reverse("user-detail", kwargs={"pk": user.pk})

    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert "username" in response.data
    assert "bio" in response.data

    assert "email" not in response.data
    assert "country" not in response.data
    assert "city" not in response.data


@pytest.mark.django_db
def test_user_detail_view_admin(admin_client, user):
    url = reverse("user-detail", kwargs={"pk": user.pk})

    response = admin_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert "is_staff" in response.data
    assert "is_active" in response.data
    assert "is_superuser" in response.data


@pytest.mark.django_db
def test_me_view_authenticated_user(auth_client, country_factory, city_factory):
    url = reverse("me")

    response = auth_client.get(url)
    data = response.data

    assert response.status_code == status.HTTP_200_OK

    assert "username" in data
    assert "bio" in data
    assert "email" in data
    assert "country" in data
    assert "city" in data

    updated_country = country_factory(name="updated country")
    updated_city = city_factory(
        name="updated city",
        country=updated_country,
    )

    data = {
        "username": "updateduser",
        "email": "updated@example.com",
        "bio": "updatedbio",
        "country": updated_country.id,
        "city": updated_city.id,
    }
    response = auth_client.put(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == "updateduser"
    assert response.data["email"] == "updated@example.com"
    assert response.data["bio"] == "updatedbio"
    # assert response.data['country'] == updated_country.id.name
    # assert response.data['city'] == updated_city.id.name


@pytest.mark.django_db
def test_me_view_unauthenticated_user(api_client):
    url = reverse("me")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_403_FORBIDDEN
