# flake8: noqa F401

from config.env import env

if env('DJANGO_ENV', default='local') == 'prod':
    from .prod import *  # Import production settings
else:
    from .local import *  # Import local settings
