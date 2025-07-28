from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import Event
from .serializers import EventSerializer, EventSummarySerializer
from .permissions import IsOrganizerOrReadOnly
from .services import EventService
from .filters import EventFilter


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsOrganizerOrReadOnly,)
    filterset_class = EventFilter

    def get_serializer_class(self):
        if self.action == "list":
            return EventSummarySerializer
        return EventSerializer

    @extend_schema(
        summary="Attend an event",
        description="Adds the authenticated user as an attendee to the event.",
        responses={
            200: OpenApiResponse(description="Successfully joined the event."),
            400: OpenApiResponse(
                description="Validation error (e.g. already attending)."
            ),
            403: OpenApiResponse(description="Authentication required."),
            500: OpenApiResponse(description="Internal server error."),
        },
    )
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def attend(self, request, pk=None):
        event = self.get_object()
        message = EventService.add_attendee(event, request.user)
        return Response({"detail": message}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Unattend an event",
        description="Removes the authenticated user from the event's attendee list.",
        responses={
            204: OpenApiResponse(description="Successfully left the event."),
            400: OpenApiResponse(description="Validation error (e.g. not attending)."),
            403: OpenApiResponse(description="Authentication required."),
            500: OpenApiResponse(description="Internal server error."),
        },
    )
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def unattend(self, request, pk=None):
        event = self.get_object()
        message = EventService.remove_attendee(event, request.user)
        return Response({"detail": message}, status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
