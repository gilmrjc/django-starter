#!/usr/bin/env bash

help () {
  # Auto document the script
  # Add "## description" after the command case to use it as the help text.
  echo "Usage: $0 command [args]"
  echo
  echo "Available commands:"
  grep -E "[a-zA-Z_-]+).*?## .*$" $0 | awk 'BEGIN {FS = ").*##"}; {printf "\033[36m%-30s\033[0m%s\n", $1, $2}'
}

run_web () {
  # Run a command in a Django container
  docker-compose run --entrypoint "$@" -w "/usr/src/app" --rm --no-deps web
}

run_django () {
  # Run a Django command
  docker-compose run --rm web python manage.py $@
}

run_npm () {
  # Run a Django command
  docker-compose run --entrypoint "npm" --rm frontend $@
}

if [ $# -lt 1 ]; then
  help
  exit
fi

command=$1
shift
args=$@

case "$command" in
# General purpose helpers) ## .
  start) ## Run the django server along with the frontend building pipeline
    docker-compose up -d web jobs frontend $args
    ;;
  logs) ## Show the services logs
    docker-compose logs -f --tail 20 web frontend $args
    ;;
  stop) ## Stop the services
    docker-compose stop $args
    ;;
  exec) ## Execute a command in the Django container
    run_web "$args"
    ;;
  shell) ## Open a shell in the Django container
    run_web "sh"
    ;;
  build) ## Build the web service image
    docker-compose build web jobs $args
    ;;
  down) ## Remove all containers used
    docker-compose down $args
    ;;
  clean) ## Remove all containers used and the volumes (erases containers data)
    docker-compose down -v $args
    ;;
# Python helpers) ## .
  pdm) ## Run pdm in a Django container
    run_web "pdm $args"
    ;;
  python-lint) ## Check python linting
    echo "PEP8 rules"
    run_web "pdm run lint:flake8"
    echo "Running black"
    run_web "pdm run lint:black"
    echo "Running pylinter"
    run_web "pdm run lint:pylint"
    ;;
  python-lint-fix) ## Fix python linting errors
    echo "Comforming to PEP8"
    run_web "pdm run lint:fix:autopep8"
    echo "Running black"
    run_web "pdm run lint:fix:black"
    echo "Sorting python imports"
    run_web "pdm run lint:fix:isort"
    echo "Prefer modern python syntax"
    run_web "pdm run lint:fix:pyupgrade"
    ;;
  python-test) ## Run python tests
    run_web "pdm run test $args"
    ;;
  python-test-watch) ## Run python tests on watch mode
    run_web "pdm run test $args"
    ;;
# Django helpers) ## .
  django) ## Run a Django command
    run_django "$args"
    ;;
  makemigrations) ## Create Django migrations
    run_django "makemigrations $args"
    ;;
  migrate) ## Run Django migrations
    run_django "migrate $args"
    ;;
  show-urls) ## Display all the Django urls
    run_django "show_urls -u $args"
    ;;
  django-shell) ## Open a shell with Django utilies loaded
    run_django "shell_plus $args"
    ;;
# Javascript helpers) ## .
  javascript-lint) ## Check javascript linting
    run_npm "run lint -- $args"
    ;;
  javascript-lint-fix) ## Fix javascript linting errors
    run_npm "run lint:fix -- $args"
    ;;
  javascript-test) ## Run javascript tests
    run_npm "run test -- $args"
    ;;
  javascript-test-watch) ## Run javascript tests on watch mode
    run_npm "run test:watch -- $args"
    ;;
  javascript-check-types) ## Check TypeScript types
    run_npm "run checkTypes -- $args"
    ;;
  *)
    echo "Invalid command: $command"
    echo
    echo
    help
    ;;
esac
