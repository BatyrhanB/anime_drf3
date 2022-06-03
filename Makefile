make_migr:
	docker-compose run --rm carp sh -c "python manage.py makemigrations"
migr:
	docker-compose run --rm carp sh -c "python manage.py migrate"
test:
	docker-compose run --rm carp sh -c "python manage.py test"
super:
	docker-compose run --rm carp sh -c "python manage.py createsuperuser"
makesuper:
	docker-compose run --rm carp sh -c "python manage.py makesuperuser"
shell:
	docker-compose run --rm carp sh -c "python manage.py shell"
ssh_w:
	docker-compose exec carp sh
test_prod:
	docker-compose -f docker-compose.prod.yml run --rm carp sh -c "python manage.py test"
wait_for_db:
	docker-compose run --rm carp sh -c "python manage.py wait_for_db"