import pytest
from django.urls import reverse
from unittest.mock import patch
from rest_framework import status

from api.accounts.utils import generate_reset_token


@pytest.mark.django_db
def test_register_view(api_client, country):
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'country': country.id,
    }
    url = reverse('register')
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert 'successfully' in response.data['detail']


@pytest.mark.django_db
@patch('api.accounts.views.send_password_reset_email')
def test_reset_password_request_view(mock_send_email, user, api_client):
    url = reverse('reset-password-request')
    data = {'email': user.email}
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert 'sent' in response.data['detail']
    mock_send_email.assert_called_once()

    args, kwargs = mock_send_email.call_args
    assert kwargs['user'] == user


@pytest.mark.django_db
def test_reset_password_request_view_no_email(api_client):
    data = {'email': ''}
    url = reverse('reset-password-request')
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'email' in response.data


@pytest.mark.django_db
def test_reset_password_request_view_invalid_email(api_client):
    data = {'email': 'nonexistent@example.com'}
    url = reverse('reset-password-request')
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'email' in response.data


@pytest.mark.django_db
def test_reset_password_confirm_view(user, api_client):
    token = generate_reset_token(user)
    url = reverse('reset-password-confirm') + f'?token={token}'
    data = {
        'new_password': 'new_secure_pass123',
        'confirm_password': 'new_secure_pass123',
    }

    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['detail'] == 'Password has been successfully changed.'
    user.refresh_from_db()
    assert user.check_password('new_secure_pass123')


@pytest.mark.django_db
def test_reset_password_confirm_view_no_token(api_client):
    url = reverse('reset-password-confirm')
    data = {
        'new_password': 'somepassword123',
        'confirm_password': 'somepassword123',
    }

    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'detail' in response.data


@pytest.mark.django_db
def test_reset_password_confirm_view_invalid_token(api_client):
    url = reverse('reset-password-confirm') + '?token=invalidtoken123'
    data = {
        'new_password': 'somepassword123',
        'confirm_password': 'somepassword123',
    }

    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'detail' in response.data


@pytest.mark.django_db
def test_reset_password_confirm_view_mismatched_passwords(user, api_client):
    token = generate_reset_token(user)
    url = reverse('reset-password-confirm') + f'?token={token}'
    data = {
        'new_password': 'testpassword1',
        'confirm_password': 'testpassword2',
    }

    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'non_field_errors' in response.data
