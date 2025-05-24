from django.contrib import admin
from .accounts.models import User
from .core.models import Country, City
from .events.models import Event

admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Event)
