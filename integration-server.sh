export COMPOSE_PROJECT_NAME=integration-testing
export DJANGO_STATIC_URL="http://localhost:8080/static/"
export DJANGO_MEDIA_URL="http://localhost:8080/media/"

echo "Building services"
docker-compose -f docker-compose.test.yml build web

echo "Running test server"
docker-compose -f docker-compose.test.yml run web python manage.py seeddb
docker-compose -f docker-compose.test.yml up web

echo "Stopping docker compose..."
docker-compose -f docker-compose.test.yml down -v
