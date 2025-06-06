import os
import django

# Update this if your settings module path is different!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from api.core.models import Country, City


# --- YOU CAN EDIT THIS DATA ---
COUNTRIES = [
    {'name': 'USA', 'code': 'US'},
    {'name': 'Germany', 'code': 'DE'},
    {'name': 'France', 'code': 'FR'},
]
CITIES = [
    {'name': 'New York', 'country_code': 'US'},
    {'name': 'Berlin', 'country_code': 'DE'},
    {'name': 'Paris', 'country_code': 'FR'},
]


def main():
    # Seed countries
    for country in COUNTRIES:
        Country.objects.get_or_create(
            code=country['code'], defaults={'name': country['name']}
        )

    # Seed cities
    for city in CITIES:
        try:
            country = Country.objects.get(code=city['country_code'])
            City.objects.get_or_create(
                name=city['name'], defaults={'country': country}
            )
        except Country.DoesNotExist:
            print(f"Country with code {city['country_code']} does not exist for city {city['name']}.")
            continue


if __name__ == '__main__':
    main()
