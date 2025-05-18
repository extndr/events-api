from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Event
from api.users.serializers import UserSummarySerializer

User = get_user_model()


class EventSerializer(serializers.HyperlinkedModelSerializer):
    organizer = UserSummarySerializer(read_only=True)
    attendees = UserSummarySerializer(many=True, read_only=True)
    attendees_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'about',
            'organizer',
            'capacity',
            'city',
            'location',
            'start_time',
            'end_time',
            'attendees',
            'attendees_count',
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


class EventSummarySerializer(EventSerializer):
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
