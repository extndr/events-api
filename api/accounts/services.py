from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserService:
    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        if User.objects.filter(username=username).exists():
            raise ValidationError({"username": "This username is already taken."})

        if User.objects.filter(email=email).exists():
            raise ValidationError({"email": "This email is already registered."})

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return user
        except Exception as e:
            raise ValidationError({"error": f"An error occurred: {str(e)}"})
