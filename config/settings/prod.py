from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', 'postgres'),
        'USER': config('DB_USER', 'postgres'),
        'PASSWORD': config('DB_PASSWORD', ''),
        'HOST': config('DB_HOST', 'localhost'),
        'PORT': config('DB_PORT', 5432),
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)
