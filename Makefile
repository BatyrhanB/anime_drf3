# Creates new migration(s) for apps.
make_migr:
	docker-compose run --rm carp sh -c "python manage.py makemigrations"

# Updates database schema. Manages both apps with migrations and those without.
migr:
	docker-compose run --rm carp sh -c "python manage.py migrate"

# Shows all available migrations for the current project
show_migr:
	docker-compose run --rm carp sh -c "python manage.py show migrations"

# Discover and run tests in the specified modules or the current directory.
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