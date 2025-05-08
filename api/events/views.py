from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.core.permissions import IsSelfOrReadOnly
from .models import Attendee, Event
from .serializers import EventSerializer, AttendeeSerializer
from .permissions import IsOrganizerOrReadOnly


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOrganizerOrReadOnly,)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=(IsAuthenticated,),
        url_path='attend'
    )
    def attend(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if Attendee.objects.filter(user=user, event=event).exists():
            return Response({
                'detail': 'You are already attending this event.'
            }, status=400)

        Attendee.objects.create(user=user, event=event)
        return Response({
            'detail': 'You are now attending the event.'
        }, status=200)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=(IsAuthenticated,),
        url_path='leave'
    )
    def leave(self, request, pk=None):
        event = self.get_object()
        user = request.user

        attendee = Attendee.objects.filter(user=user, event=event).first()
        if not attendee:
            return Response({
                'detail': 'You are not attending this event.'
            }, status=status.HTTP_400_BAD_REQUEST)

        attendee.delete()
        return Response({
            'detail': 'You have successfully left the event.'
        }, status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class AttendeeViewSet(ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = (IsSelfOrReadOnly,)
