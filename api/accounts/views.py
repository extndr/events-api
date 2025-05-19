from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import (
    UserRegisterSerializer,
    ResetPasswordRequestSerializer,
    ResetPasswordConfirmSerializer
)
from .services import UserService
from .utils import send_password_reset_email

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class ResetPasswordRequestView(generics.GenericAPIView):
    serializer_class = ResetPasswordRequestSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            send_password_reset_email(email=email, request=request)
            return Response(
                {"detail": "Password reset link has been sent to your email."},
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        token = self.request.query_params.get('token')

        if not token:
            raise ValidationError({"detail": "Token not found."})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data['new_password']

        UserService.reset_password(token, new_password)
        return Response({"detail": "Password has been successfully changed."}, status=status.HTTP_200_OK)
