start:
	poetry run flask --app modifying_forms_flask.app run --port 8000

start-debug:
	poetry run flask --app modifying_forms_flask.app run --debug --port 8000