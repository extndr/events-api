from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserService:
    @staticmethod
    def create_user(username: str, email: str, password: str) -> dict:
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
