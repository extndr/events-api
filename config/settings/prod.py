# flake8: noqa F401, F403

from .base import *
from config.env import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ("rest_framework.renderers.JSONRenderer",)

# Email (SendGrid)
# https://sendgrid.com/docs/
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env("SENDGRID_API_KEY")
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_ECHO_TO_STDOUT = False
