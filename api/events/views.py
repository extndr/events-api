from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Event
from .serializers import EventSerializer, EventShortSerializer
from .permissions import IsOrganizerOrReadOnly
from .services import EventService
from .filters import EventFilter


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsOrganizerOrReadOnly,)
    filterset_class = EventFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return EventShortSerializer
        return EventSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def attend(self, request, pk=None):
        event = self.get_object()
        message = EventService.add_attendee(event, request.user)
        return Response({'detail': message}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unattend(self, request, pk=None):
        event = self.get_object()
        message = EventService.remove_attendee(event, request.user)
        return Response({'detail': message}, status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        EventService.create_event(serializer, self.request.user)
