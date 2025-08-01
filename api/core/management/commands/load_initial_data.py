from django.core.management.base import BaseCommand
from django.core.management import call_command
from api.core.models import Country, City
from api.events.models import Event
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Load initial fixture data if not already loaded.'

    fixtures = [
        ('Countries', Country, '../fixtures/countries.json'),
        ('Cities', City, '../fixtures/cities.json'),
        ('Events', Event, '../fixtures/events.json'),
    ]

    def create_temp_user(self):
        temp_user, created = User.objects.get_or_create(username='tempuser')
        if created:
            temp_user.set_password('temppassword')
            temp_user.save()
            self.stdout.write('Temporary user created.')
        return temp_user

    def delete_temp_user(self, temp_user):
        temp_user.delete()
        self.stdout.write('Temporary user deleted.')

    def load_fixture_if_needed(self, name, model, fixture_path):
        if model.objects.exists():
            self.stdout.write(self.style.SUCCESS(f'{name} already loaded, skipping.'))
            return False
        self.stdout.write(f'Loading {name.lower()} fixture...')
        call_command('loaddata', fixture_path)
        self.stdout.write(self.style.SUCCESS(f'{name} loaded.'))
        return True

    def handle(self, *args, **kwargs):
        temp_user = self.create_temp_user()

        for name, model, fixture_path in self.fixtures:
            self.load_fixture_if_needed(name, model, fixture_path)

        self.delete_temp_user(temp_user)
