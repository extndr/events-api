from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from .serializers import (
    UserRegisterSerializer,
    ResetPasswordRequestSerializer,
    ResetPasswordConfirmSerializer,
)
from .models import User
from .services import UserService
from .utils import send_password_reset_email


@extend_schema(
    summary="Register a new user",
    description="Registers a new user using username, email, password, and country ID.",
    request=UserRegisterSerializer,
    responses={
        201: OpenApiResponse(description="User registered successfully"),
        400: OpenApiResponse(description="Bad request, invalid data"),
        500: OpenApiResponse(description="Internal server error"),
    },
)
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "User registered successfully"}, status=status.HTTP_201_CREATED
        )


@extend_schema(
    summary="Request password reset",
    description="Sends a password reset link to the user's email if the account exists.",
    request=ResetPasswordRequestSerializer,
    responses={
        200: OpenApiResponse(description="Password reset link sent"),
        400: OpenApiResponse(description="Invalid email or bad request"),
        500: OpenApiResponse(description="Internal server error"),
    },
)
class ResetPasswordRequestView(generics.GenericAPIView):
    serializer_class = ResetPasswordRequestSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        user = User.objects.get(email=email)

        send_password_reset_email(user=user, request=request)
        return Response(
            {"detail": "Password reset link has been sent to your email."},
            status=status.HTTP_200_OK,
        )


@extend_schema(
    summary="Confirm password reset",
    description="Sets a new password using a token from email. "
    "Token must be passed as a query parameter (?token=...).",
    request=ResetPasswordConfirmSerializer,
    parameters=[
        OpenApiParameter(
            name="token",
            type=str,
            location=OpenApiParameter.QUERY,
            required=True,
            description="Password reset token from email",
        )
    ],
    responses={
        200: OpenApiResponse(description="Password has been successfully changed."),
        400: OpenApiResponse(description="Bad request, invalid token or data"),
        500: OpenApiResponse(description="Internal server error"),
    },
)
class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        token = self.request.query_params.get("token")

        if not token:
            raise ValidationError({"detail": "Token not found."})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data["new_password"]

        UserService.reset_password(token, new_password)
        return Response(
            {"detail": "Password has been successfully changed."},
            status=status.HTTP_200_OK,
        )
