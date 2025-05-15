from rest_framework.exceptions import ValidationError

from api.users.models import Profile


class ProfileService:
    @staticmethod
    def create_profile(user):
        try:
            profile = Profile.objects.create(user=user)
            return profile
        except Exception as e:
            raise ValidationError({"error": f"Error creating profile: {str(e)}"})

    @staticmethod
    def get_profile(user):
        try:
            return user.profile
        except Profile.DoesNotExist:
            raise ValidationError({"detail": "Profile does not exist."})

    @staticmethod
    def update_profile(profile, data):
        try:
            profile.bio = data.get('bio', profile.bio)
            profile.location = data.get('location', profile.location)
            profile.save()
            return profile
        except Exception as e:
            raise ValidationError({"error": f"Error updating profile: {str(e)}"})
