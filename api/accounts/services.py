from rest_framework.exceptions import ValidationError
from .models import User
from .utils import get_user_from_token


class UserService:
    @staticmethod
    def create_user(username, email, password, country) -> User:
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                country=country,
            )

            return user
        except Exception as e:
            raise ValidationError({"error": f"An error occurred: {str(e)}"})

    @staticmethod
    def reset_password(token: str, new_password: str):
        user = get_user_from_token(token)

        if user is None:
            raise ValidationError({"detail": "Invalid or expired token."})

        user.set_password(new_password)
        user.save()
        return user
