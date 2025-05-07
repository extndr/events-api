from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'city',
            'location',
            'organizer',
            'start_time',
            'end_time',
        )

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
