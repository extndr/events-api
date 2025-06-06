from decouple import config

env = config('DJANGO_ENV', default='local').lower()

if env == 'prod':
    from .prod import *  # Import production settings
else:
    from .local import *  # Import local settings
