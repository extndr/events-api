from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    UserDetailSerializer,
    EnhancedUserSerializer,
    UserSummarySerializer,
    PrivateUserSerializer,
)
from api.core.permissions import IsSelfOrReadOnly

User = get_user_model()


@extend_schema(
    summary="Retrieve a list of users",
    description="Returns a list of all users with basic information.",
    responses={
        200: OpenApiResponse(description="List of users retrieved successfully"),
        400: OpenApiResponse(
            description="Bad request (e.g., invalid query parameters)."
        ),
        500: OpenApiResponse(description="Internal server error."),
    },
)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSummarySerializer
    permission_classes = (AllowAny,)


@extend_schema(
    summary="Retrieve or update user details",
    description="Retrieve details of the authenticated user, or update them if authorized.",
    responses={
        200: OpenApiResponse(description="User details retrieved successfully."),
        400: OpenApiResponse(description="Bad request (e.g., invalid input)."),
        403: OpenApiResponse(description="Authentication required."),
        404: OpenApiResponse(description="User not found."),
        500: OpenApiResponse(description="Internal server error."),
    },
)
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsSelfOrReadOnly,
    )

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return EnhancedUserSerializer
        return UserDetailSerializer


@extend_schema(
    summary="Retrieve or update the authenticated user's details",
    description="Retrieve or update the details of the currently authenticated user.",
    responses={
        200: OpenApiResponse(
            description="User details retrieved or updated successfully."
        ),
        400: OpenApiResponse(description="Bad request (validation errors)."),
        401: OpenApiResponse(description="Authentication required."),
        403: OpenApiResponse(
            description="Forbidden access (insufficient permissions)."
        ),
        500: OpenApiResponse(description="Internal server error."),
    },
)
class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = PrivateUserSerializer

    def get_object(self):
        return self.request.user
