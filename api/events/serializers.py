from rest_framework import serializers
from .models import Country, City, Event


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

    def to_representation(self, instance):
        rep = super(CitySerializer, self).to_representation(instance)
        rep['country'] = instance.country.name
        return rep


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'city',
            'location',
            'organizer',
            'start_time',
            'end_time',
        ]

    def to_representation(self, instance):
        rep = super(EventSerializer, self).to_representation(instance)
        rep['city'] = instance.city.name
        rep['organizer'] = instance.organizer.username
        return rep
