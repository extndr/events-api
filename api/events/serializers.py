from django.utils import timezone
from rest_framework import serializers
from .models import Event, Attendee


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'organizer',
            'city',
            'location',
            'start_time',
            'end_time',
        )
        read_only_fields = ('organizer',)

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time and end_time:
            if end_time <= start_time:
                raise serializers.ValidationError(
                    "End time must be after start time."
                )
            if start_time < timezone.now():
                raise serializers.ValidationError(
                    "Event cannot start in the past."
                )

        return data

    def to_representation(self, instance):
        rep = super(EventSerializer, self).to_representation(instance)
        rep['city'] = instance.city.name
        rep['organizer'] = instance.organizer.username
        return rep


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ('user', 'event', 'joined_at')

    def to_representation(self, instance):
        rep = super(AttendeeSerializer, self).to_representation(instance)
        rep['user'] = instance.user.username
        rep['event'] = instance.event.title
        return rep
