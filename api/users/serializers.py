from django.contrib.auth.models import User
from rest_framework import serializers

from api.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'bio', 'location')
        read_only_fields = ('id', 'username')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'email', 'is_active', 'is_staff', 'is_superuser')
