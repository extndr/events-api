import pytest
from unittest.mock import patch
from api.accounts.services import UserService


@pytest.mark.django_db
def test_register_user(country):
    data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "testpassword",
        "country": country,
    }
    user = UserService.register_user(**data)

    assert user.username == data["username"]
    assert user.email == data["email"]
    assert user.country == data["country"]
    assert user.check_password(data["password"])


@pytest.mark.django_db
@patch("api.accounts.services.get_user_from_token")
def test_reset_password(mock_get_user_from_token, user):
    user.set_password("oldpassword")
    user.save()

    mock_get_user_from_token.return_value = user

    UserService.reset_password("fake_token", "newpassword")
    user.refresh_from_db()

    assert user.check_password("newpassword")
