#!/bin/sh

set -e

echo "Running Database Migrations"
python manage.py migrate

if [ "$DJANGO_ENV" = "prod" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
fi

echo "Seeding data (countries, cities)..."
python seed_data.py

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000

exec "$@"
