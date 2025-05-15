import django_filters
from .models import Profile


class ProfileFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name='user__username',
        lookup_expr='iexact'
    )
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Profile
        fields = ('username', 'location')
