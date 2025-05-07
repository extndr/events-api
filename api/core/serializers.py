from .models import Country, City
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country')

    def to_representation(self, instance):
        rep = super(CitySerializer, self).to_representation(instance)
        rep['country'] = instance.country.name
        return rep
