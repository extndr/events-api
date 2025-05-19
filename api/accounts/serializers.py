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


class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords don't match.")
        return data
