from .models import Country, City
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        min_length=2, help_text="Country code (unique, min/max. 2 letters)"
    )

    class Meta:
        model = Country
        fields = ("id", "name", "code")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "country")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["country"] = instance.country.name
        return rep
