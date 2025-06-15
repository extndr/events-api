#!/bin/sh

set -e

export PYTHONPATH=$PYTHONPATH:/app

echo "Waiting for database..."
python scripts/wait_for_db.py

echo "Running Database Migrations"
python manage.py migrate

echo "Seeding data (countries, cities)..."
python scripts/seed_data.py || { echo "Data seeding failed"; exit 1; }

if [ "$DJANGO_ENV" = "prod" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
fi

echo "Running server with Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
