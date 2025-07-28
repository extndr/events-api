from rest_framework.exceptions import ValidationError
from .models import User
from .utils import get_user_from_token
from api.core.models import Country


class UserService:
    """
    Service class for handling user-related business logic.
    """

    @staticmethod
    def register_user(
        username: str, email: str, password: str, country: Country
    ) -> User:
        """
        Register a new user with the given credentials and country.
        """

        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            country=country,
        )

    @staticmethod
    def reset_password(token: str, new_password: str):
        """
        Reset the user's password using a JWT token from a password reset email.

        Raises:
            ValidationError: If the token is invalid or expired.
        """

        user = get_user_from_token(token)

        if user is None:
            raise ValidationError({"detail": "Invalid or expired token."})

        user.set_password(new_password)
        user.save()
        return user
