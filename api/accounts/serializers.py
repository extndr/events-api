from django.contrib.auth.models import User
from rest_framework import serializers

from api.core.models import City
from api.accounts.services import UserService


class UserRegisterSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'city')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters.")
        return value

    def create(self, validated_data):
        return UserService.create_user(**validated_data)
