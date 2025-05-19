from datetime import timedelta

from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail

from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


User = get_user_model()


def generate_reset_token(user):
    refresh = RefreshToken.for_user(user)
    refresh.set_exp(lifetime=timedelta(minutes=30))
    return str(refresh.access_token)


def get_user_from_token(token):
    try:
        access = AccessToken(token)
        return User.objects.get(id=access['user_id'])
    except Exception:
        return None


def build_password_reset_url(email: str, request) -> str:
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError({"detail": "User with this email not found."})

    token = generate_reset_token(user)
    reset_url = request.build_absolute_uri(
        reverse("reset-password-confirm")
    ) + f"?token={token}"
    return reset_url


def send_password_reset_email(email: str, request):
    reset_url = build_password_reset_url(email=email, request=request)
    send_mail(
        'Password Reset',
        f'Click the link to reset your password: {reset_url}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
    return reset_url
