install:
    @cp .env-example .env
    @docker-compose build
    @docker-compose up -d
    @sleep 30
    @docker-compose run web npm install
    @docker-compose run web python manage.py migrate
    @docker-compose stop

build:
    @@docker-compose build

up:
    @docker-compose up

stop:
    @docker-compose stop

superuser:
    @docker-compose run web python manage.py createsuperuser

shell:
    @docker-compose run web python manage.py shell_plus

watch:
    @docker-compose run web gulp watch

assets:
    @docker-compose run web gulp build

test:
    @docker-compose run web coverage run --source=. --omit=*/wsgi.py manage.py test
    @docker-compose run web coverage report
    @docker-compose run web coverage html

clear:
    @rm -fr bower_components/
    @rm -fr node_modules/
    @rm -fr .coverage
    @rm -fr html_cov/
