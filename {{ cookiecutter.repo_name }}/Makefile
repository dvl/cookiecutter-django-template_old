serve:
	@python manage.py runserver 0.0.0.0:8000

test:
	@export REUSE_DB=1
	@coverage run --source={{ cookiecutter.project_name }}/ --omit=*/wsgi.py manage.py test
	@coverage report
	@coverage html

clear:
	@rm -fr bower_components/
	@rm -fr node_modules/
	@rm -fr .coverage
	@rm -fr html_cov/
