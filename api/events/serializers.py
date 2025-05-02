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

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time and end_time:
            if end_time <= start_time:
                raise serializers.ValidationError(
                    "End time must be after start time."
                )
        return data

    def to_representation(self, instance):
        rep = super(EventSerializer, self).to_representation(instance)
        rep['city'] = instance.city.name
        rep['organizer'] = instance.organizer.username
        return rep
