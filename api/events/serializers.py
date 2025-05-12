from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers

from api.accounts.serializers import ProfileSerializer
from .models import Event


class AttendeeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'profile')


class OrganizerSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'profile')


class EventSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer(read_only=True)
    attendees = AttendeeSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'about',
            'organizer',
            'city',
            'location',
            'start_time',
            'end_time',
            'attendees'
        )

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
        rep = super().to_representation(instance)
        rep['city'] = instance.city.name
        return rep
