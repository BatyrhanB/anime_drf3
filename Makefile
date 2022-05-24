make_migr:
	docker-compose run --rm carp sh -c "python manage.py makemigrations bank"
migr:
	docker-compose run --rm carp sh -c "python manage.py migrate"
test:
	docker-compose run --rm carp sh -c "python manage.py test"
super:
	docker-compose run --rm carp sh -c "python manage.py createsuperuser"
shell:
	docker-compose run --rm carp sh -c "python manage.py shell"
ssh_w:
	docker-compose exec carp sh
test_prod:
	docker-compose -f docker-compose.prod.yml run --rm carp sh -c "python manage.py test"