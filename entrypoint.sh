#!/bin/bash

set -e

echo "Running Database Migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running server with Gunicorn..."
exec gunicorn config.wsgi:application --bind ${APP_HOST}:${APP_PORT}
