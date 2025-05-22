from rest_framework.exceptions import ValidationError
from .models import User
from .utils import get_user_from_token
from api.core.models import Country


class UserService:
    @staticmethod
    def register_user(username: str, email: str, password: str, country: Country) -> User:
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            country=country,
        )

    @staticmethod
    def reset_password(token: str, new_password: str):
        user = get_user_from_token(token)

        if user is None:
            raise ValidationError({"detail": "Invalid or expired token."})

        user.set_password(new_password)
        user.save()
        return user
