import django_filters
from .models import Event


class EventFilter(django_filters.FilterSet):
    """
    Filter events by start time, end time, organizer, country and city.
    """

    start_time = django_filters.DateTimeFilter(
        field_name="start_time", lookup_expr="gte"
    )
    end_time = django_filters.DateTimeFilter(field_name="end_time", lookup_expr="lte")
    organizer = django_filters.CharFilter(
        field_name="organizer__username", lookup_expr="iexact"
    )
    country = django_filters.CharFilter(
        field_name="city__country__code", lookup_expr="iexact", label="Country code"
    )
    city = django_filters.CharFilter(field_name="city__name", lookup_expr="iexact")

    class Meta:
        model = Event
        fields = ("start_time", "end_time", "organizer", "country", "city")
