from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Attendee, Event
from .serializers import EventSerializer, AttendeeSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(
        detail=True,
        methods=['post'],
        permission_classes=(IsAuthenticated,)
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

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class AttendeeViewSet(ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
