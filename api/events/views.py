from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from .permissions import IsOrganizerOrReadOnly
from .services import attend_event, unattend_event


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOrganizerOrReadOnly,)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def attend(self, request, pk=None):
        event = self.get_object()
        try:
            message = attend_event(event, request.user)
            return Response({'detail': message}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unattend(self, request, pk=None):
        event = self.get_object()
        try:
            message = unattend_event(event, request.user)
            return Response({'detail': message}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
