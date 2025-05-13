import django_filters
from .models import City


class CityFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(
        field_name='country__name',
        lookup_expr='iexact'
    )

    class Meta:
        model = City
        fields = ('country',)
