from rest_framework.viewsets import ModelViewSet
from .models import Country, City
from .serializers import CountrySerializer, CitySerializer
from .permissions import IsAdminOrReadOnly
from .filters import CityFilter


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAdminOrReadOnly,)


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = CityFilter
