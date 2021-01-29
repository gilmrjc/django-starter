#!/bin/sh

echo "Waiting for database..."

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 1
done

echo "Database started"

if [ -z "$SKIP_SETUP_JOBS" ]
then
  echo "Run setup jobs"
  pdm run python manage.py migrate --no-input
  pdm run python manage.py collectstatic --no-input
else
  echo "Skip setup jobs"
fi

pdm run "$@"
