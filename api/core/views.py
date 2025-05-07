from rest_framework.viewsets import ModelViewSet
from .models import Country, City
from .serializers import CountrySerializer, CitySerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
