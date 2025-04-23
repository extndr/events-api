#!/bin/sh

echo "Running Database Migrations"
python manage.py migrate

echo "Running server..."
python manage.py runserver 0.0.0.0:8000

exec "$@"
