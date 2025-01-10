install-lib:

install-libdev:
	poetry add --group dev isort
	poetry add --group dev black
	poetry add --group dev flake8
	poetry add --group dev pytest-django

quality:
	poetry run isort .
	poetry run black .
	poetry run flake8 .

runserver:
	poetry run runserver