import pytest
import uuid

from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from api.core.models import Country, City
from api.accounts.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def admin_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def country_factory():
    def create_country(name='testcountry'):
        return Country.objects.create(name=name)
    return create_country


@pytest.fixture
def city_factory(country):
    def create_city(name='testcity', country=country):
        return City.objects.create(name=name, country=country)
    return create_city


@pytest.fixture
def user_factory(country):
    def create_user(**kwargs):
        # generate unique 8-character id using uuid
        uid = uuid.uuid4().hex[:8]
        defaults = {
            'username': f'user_{uid}',  # unique username with uid
            'email': f'{uid}@example.com',  # unique email with uid
            'password': 'testpassword',
            'country': country,
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)

    return create_user


@pytest.fixture
def country(country_factory):
    return country_factory()


@pytest.fixture
def city(city_factory):
    return city_factory()


@pytest.fixture
def user(user_factory):
    return user_factory(
        username='testuser',
        email='testuser@email.com',
        password='testpassword',
        is_staff=False,
    )


@pytest.fixture
def admin_user(user_factory):
    return user_factory(
        is_staff=True,
        is_superuser=True,
    )
