install:
	poetry install && cp config/.env.template config/.env

runserver:
	poetry run python manage.py runserver

fakemigrate:
	poetry run python manage.py migrate movies --fake && poetry run python manage.py migrate

createsuperuser:
	poetry run python manage.py createsuperuser

up-dev:
	docker-compose up --build -d

up-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

down:
	docker-compose down --remove-orphans

dev-fakemigrate:
	docker-compose run --rm web python manage.py migrate movies --fake && docker-compose run --rm web python manage.py migrate

prod-fakemigrate:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --rm web python manage.py migrate movies --fake && docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --rm web python manage.py migrate

dev-createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

prod-createsuperuser:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --rm web python manage.py createsuperuser

dev-logs:
	docker-compose logs -f

prod-logs:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml logs -f
