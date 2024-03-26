#!/bin/bash
set -e

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@gmail.com"}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"admin"}
APP_PORT=${APP_PORT:-8000}

echo "Running Production Server"
pip install -r requirements/production.txt
python manage.py migrate --noinput --settings=technoshop.settings.production
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --settings=technoshop.settings.production || true
gunicorn --worker-tmp-dir /dev/shm --workers 3 technoshop.wsgi:application --bind "0.0.0.0:${APP_PORT}"
