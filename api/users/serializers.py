from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "bio",
        )


class UserSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "url",
        )


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "bio",
            "email",
            "country",
            "city",
            "url",
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.country:
            rep["country"] = instance.country.name
        if instance.city:
            rep["city"] = instance.city.name
        return rep


class EnhancedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "bio",
            "is_active",
            "is_staff",
            "is_superuser",
        )
