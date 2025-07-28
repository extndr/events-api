import pytest
from api.core.serializers import CitySerializer


@pytest.mark.django_db
def test_city_serializer_output(city, country):
    serializer = CitySerializer(city)
    data = serializer.data

    assert data["name"] == city.name
    assert data["country"] == country.name


@pytest.mark.django_db
def test_city_serializer_input_valid(country):
    data = {"name": "Sample City", "country": country.id}
    serializer = CitySerializer(data=data)

    assert serializer.is_valid()
    city = serializer.save()

    assert city.name == data["name"]
    assert city.country == country


@pytest.mark.django_db
def test_city_serializer_input_invalid_country():
    data = {
        "name": "Sample City",
        "country": 9999,
    }
    serializer = CitySerializer(data=data)

    assert not serializer.is_valid()
    assert "country" in serializer.errors


@pytest.mark.django_db
def test_city_serializer_invalid_missing_fields():
    data = {
        "name": "",
        "country": "",
    }
    serializer = CitySerializer(data=data)

    assert not serializer.is_valid()
    assert "name" in serializer.errors
    assert "country" in serializer.errors
