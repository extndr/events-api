from rest_framework import serializers

from api.core.models import Country

from .models import User
from .services import UserService


class UserRegisterSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), write_only=True
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'country', 'email', 'password')

    def create(self, validated_data):
        return UserService.create_user(**validated_data)
