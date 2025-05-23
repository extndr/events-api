from datetime import timedelta

from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


User = get_user_model()


def generate_reset_token(user):
    """
    Generate a short-lived JWT access token for the given user.
    Used for password reset links.
    """

    refresh = RefreshToken.for_user(user)
    refresh.set_exp(lifetime=timedelta(minutes=30))
    return str(refresh.access_token)


def get_user_from_token(token):
    """
    Retrieve the user from a given JWT access token.
    Returns None if token is invalid or expired.
    """

    try:
        access = AccessToken(token)
        return User.objects.get(id=access['user_id'])
    except Exception:
        return None


def build_password_reset_url(user, request) -> str:
    """
    Build the absolute password reset URL with token query param.
    """

    token = generate_reset_token(user)
    reset_url = request.build_absolute_uri(
        reverse("reset-password-confirm")
    ) + f"?token={token}"
    return reset_url


def send_password_reset_email(user, request):
    """
    Send a password reset email with a secure link.
    """

    reset_url = build_password_reset_url(user=user, request=request)
    send_mail(
        'Password Reset',
        f'Click the link to reset your password: {reset_url}',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
    )
    return reset_url
