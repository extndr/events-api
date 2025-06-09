import os
import time
import django

from django.db import connections
from django.db.utils import OperationalError
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

db_config = settings.DATABASES['default']

MAX_RETRIES = 30
RETRY_DELAY = 1


def check_database_connection():
    try:
        connection = connections['default']
        connection.ensure_connection()
        return True
    except OperationalError:
        return False


def wait_for_db():
    retries = 0
    while retries < MAX_RETRIES:
        if check_database_connection():
            print('Database is ready.')
            break
        else:
            retries += 1
            print(f'Database is unavailable - waiting {RETRY_DELAY} second(s)... Attempt {retries}/{MAX_RETRIES}')
            time.sleep(RETRY_DELAY)
    else:
        print(f'Max retries reached. Could not connect to the database after {MAX_RETRIES} attempts.')
        exit(1)


if __name__ == '__main__':
    wait_for_db()
