import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

from api.users.serializers import (
    UserDetailSerializer,
    UserSummarySerializer,
    PrivateUserSerializer,
    EnhancedUserSerializer
)

User = get_user_model()


@pytest.mark.django_db
def test_user_detail_serializer(user, factory):
    url = reverse('user-detail', kwargs={'pk': user.pk})

    request = factory.get(url)
    serializer = UserDetailSerializer(user, context={'request': request})

    assert serializer.data['username'] == user.username
    assert serializer.data['bio'] == user.bio


@pytest.mark.django_db
def test_user_summary_serializer(user, factory):
    request = factory.get(reverse('user-list'))
    serializer = UserSummarySerializer(user, context={'request': request})

    assert serializer.data['username'] == user.username

    assert 'url' in serializer.data
    assert 'bio' not in serializer.data


@pytest.mark.django_db
def test_private_user_serializer(user, factory):
    request = factory.get(reverse('me'))
    serializer = PrivateUserSerializer(user, context={'request': request})

    assert serializer.data['username'] == user.username
    assert serializer.data['email'] == user.email
    assert serializer.data['bio'] == user.bio

    if user.country:
        assert serializer.data['country'] == user.country.name

    if user.city:
        assert serializer.data['city'] == user.city.name


@pytest.mark.django_db
def test_enhanced_user_serializer(user, factory):
    request = factory.get(reverse('user-detail', kwargs={'pk': user.pk}))
    serializer = EnhancedUserSerializer(user, context={'request': request})

    assert serializer.data['username'] == user.username
    assert serializer.data['bio'] == user.bio
    assert serializer.data['is_active'] == user.is_active
    assert serializer.data['is_staff'] == user.is_staff
    assert serializer.data['is_superuser'] == user.is_superuser
