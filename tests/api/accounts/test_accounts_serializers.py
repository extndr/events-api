import pytest
from api.accounts.serializers import (
    UserRegisterSerializer,
    ResetPasswordRequestSerializer,
)


@pytest.mark.django_db
def test_user_register_serializer_input_valid(country):
    data = {
        "username": "newuser",
        "country": country.id,
        "email": "newuser@example.com",
        "password": "testpassword",
    }
    serializer = UserRegisterSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_user_register_serializer_input_invalid():
    data = {
        "username": "12",
        "country": 999,
        "email": "invalidemail",
        "password": "qwerty",
    }
    serializer = UserRegisterSerializer(data=data)
    assert not serializer.is_valid()

    for field in data:
        assert field in serializer.errors


@pytest.mark.django_db
def test_user_register_serializer_missing_fields():
    data = {
        "username": "",
        "country": "",
        "email": "",
        "password": "",
    }
    serializer = UserRegisterSerializer(data=data)
    assert not serializer.is_valid()

    for field in data:
        assert field in serializer.errors


@pytest.mark.django_db
def test_reset_password_request_serializer_input_valid(user):
    data = {"email": user.email}
    serializer = ResetPasswordRequestSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_reset_password_request_serializer_input_invalid():
    data = {"email": "nonexistent@example.com"}
    serializer = ResetPasswordRequestSerializer(data=data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors


@pytest.mark.django_db
def test_reset_password_request_serializer_missing_fields():
    data = {"email": ""}
    serializer = ResetPasswordRequestSerializer(data=data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors
