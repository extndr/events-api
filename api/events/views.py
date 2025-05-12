from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from .permissions import IsOrganizerOrReadOnly


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOrganizerOrReadOnly,)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=(IsAuthenticated,),
    )
    def attend(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if user in event.attendees.all():
            return Response(
                {'detail': 'You are already attending this event.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        event.attendees.add(user)
        return Response(
            {'detail': 'You are now attending the event.'},
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=['post'],
        permission_classes=(IsAuthenticated,),
    )
    def unattend(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if user not in event.attendees.all():
            return Response(
                {'detail': 'You are not attending this event.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        event.attendees.remove(user)
        return Response(
            {'detail': 'You have successfully left the event.'},
            status=status.HTTP_204_NO_CONTENT
        )

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
