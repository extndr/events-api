# flake8: noqa F403, F405

from .base import *

DEBUG = True

# Email (MailHog)
# https://github.com/mailhog/MailHog
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025

SPECTACULAR_SETTINGS = {
    "TITLE": "Events API",
    "DESCRIPTION": "API for managing users, profiles, countries, cities, and events.",
    "VERSION": "1.0.0",
}
