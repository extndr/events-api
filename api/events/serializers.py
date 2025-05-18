from django.utils import timezone
from rest_framework import serializers

from api.users.serializers import ProfileSerializer
from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    organizer = ProfileSerializer(source='organizer.profile', read_only=True)
    attendees = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='profile-detail'
    )
    attendees_count = serializers.SerializerMethodField()

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
            'attendees',
            'attendees_count',
            'capacity',
            'url'
        )

    def get_attendees_count(self, obj):
        return obj.attendees.count()

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


class EventShortSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'city',
            'capacity',
            'start_time',
            'attendees_count',
            'url'
        )
