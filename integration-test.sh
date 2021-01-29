export COMPOSE_PROJECT_NAME=integration-testing
export DJANGO_STATIC_URL="http://static.local:8080/static/"
export DJANGO_STATIC_URL="http://static.local:8080/media/"

echo "Starting services"
docker-compose -f docker-compose.test.yml up -d --build web
docker-compose -f docker-compose.test.yml run web python manage.py seeddb

echo "Building tests"
docker-compose -f docker-compose.test.yml -f docker-compose.cypress.yml build cypress

echo "Running tests"
docker-compose -f docker-compose.test.yml -f docker-compose.cypress.yml up --exit-code-from cypress -- cypress
exit_code=$?

echo "Stopping docker compose..."
docker-compose -f docker-compose.test.yml -f docker-compose.cypress.yml down -v

exit ${exit_code}
