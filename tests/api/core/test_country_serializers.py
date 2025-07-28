import pytest
from api.core.serializers import CountrySerializer


@pytest.mark.django_db
def test_country_serializer_output(country):
    serializer = CountrySerializer(country)
    data = serializer.data

    assert data["id"] == country.id
    assert data["name"] == country.name


@pytest.mark.django_db
def test_country_serializer_input_valid():
    input_data = {"name": "New Country", "code": "UK"}
    serializer = CountrySerializer(data=input_data)

    assert serializer.is_valid()
    country = serializer.save()

    assert country.name == input_data["name"]


@pytest.mark.django_db
def test_country_serializer_invalid_missing_fields():
    input_data = {"name": "", "code": ""}
    serializer = CountrySerializer(data=input_data)

    assert not serializer.is_valid()
    assert "name" in serializer.errors
    assert "code" in serializer.errors
