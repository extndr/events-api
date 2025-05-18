from rest_framework.exceptions import ValidationError

from .models import User


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
