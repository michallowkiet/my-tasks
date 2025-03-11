#!/bin/bash

echo "Starting Migrations..."
uv run manage.py migrate
echo ====================================

echo "Collecting Static Files..."
uv run manage.py collectstatic --noinput
echo ====================================

echo "Starting Server..."
uv run gunicorn my_tasks.wsgi:application --bind 0.0.0.0:8000

