from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


def register_user(username: str, email: str, password: str) -> dict:
    if User.objects.filter(email=email).exists():
        raise ValidationError("This email already exists.")

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    refresh = RefreshToken.for_user(user)
    return {
        "user": user,
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }
