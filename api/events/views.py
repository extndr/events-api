from rest_framework.viewsets import ModelViewSet
from .models import Event
from .serailizers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
