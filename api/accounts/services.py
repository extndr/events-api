from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from api.users.services import ProfileService


class UserService:
    @staticmethod
    def create_user(username, email, password, city) -> User:
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            country = city.country
            location = f"{city.name}, {country.name}"

            ProfileService.update_profile(
                profile=user.profile,
                data={"location": location}
            )

            return user
        except Exception as e:
            raise ValidationError({"error": f"An error occurred: {str(e)}"})
