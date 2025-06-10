from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.core.models import Country
from .models import User
from .services import UserService


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=3,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        required=True
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            'username',
            'country',
            'email',
            'password',
        )

    def create(self, validated_data):
        return UserService.register_user(**validated_data)


class ResetPasswordRequestSerializer(serializers.Serializer):
    """
    Serializer for password reset request. Takes user email.
    """

    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email not found.')
        return value


class ResetPasswordConfirmSerializer(serializers.Serializer):
    """
    Serializer for confirming password reset.

    Requires new_password and confirm_password. Validates that both match.
    """

    new_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password]
    )
    confirm_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
