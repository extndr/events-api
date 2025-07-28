from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Event
from api.core.models import City
from api.users.serializers import UserSummarySerializer

User = get_user_model()


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for event details.
    """

    organizer = UserSummarySerializer(read_only=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    attendees = UserSummarySerializer(many=True, read_only=True)
    attendees_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "about",
            "organizer",
            "capacity",
            "city",
            "location",
            "start_time",
            "end_time",
            "attendees",
            "attendees_count",
            "url",
        )

    def get_attendees_count(self, obj):
        """
        Get the number of attendees for the event.
        """

        return obj.attendees.count()

    def validate(self, data):
        """
        Validate the start and end times of the event.
        Ensures the event doesn't start in the past and that the end time is after the start time.
        """

        start_time = data.get("start_time")
        end_time = data.get("end_time")

        errors = {}

        if start_time and end_time:
            if end_time <= start_time:
                errors["end_time"] = "End time must be after start time."

            if start_time < timezone.now():
                errors["start_time"] = "Event cannot start in the past."

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def to_representation(self, instance):
        """
        Customize the representation of the event, including the city name.
        """

        rep = super().to_representation(instance)
        rep["city"] = instance.city.name
        return rep


class EventSummarySerializer(EventSerializer):
    """
    Serializer for a brief event summary.
    """

    class Meta(EventSerializer.Meta):
        model = Event
        fields = (
            "id",
            "title",
            "city",
            "capacity",
            "start_time",
            "attendees_count",
            "url",
        )
