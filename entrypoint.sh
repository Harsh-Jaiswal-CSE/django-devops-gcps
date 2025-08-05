#!/bin/bash
set -e

if [ "$1" = "celery" ]; then
    echo "Starting Celery worker..."
    celery -A hello_django worker --loglevel=info
else
    echo "Starting Django with Gunicorn..."
    gunicorn hello_django.wsgi:application --bind 0.0.0.0:8000
fi
