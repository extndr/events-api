import django_filters
from .models import City


class CityFilter(django_filters.FilterSet):
    """
    Filter cities by country code (case-insensitive).
    """

    country = django_filters.CharFilter(
        field_name='country__code',
        lookup_expr='iexact'
    )

    class Meta:
        model = City
        fields = ('country',)
