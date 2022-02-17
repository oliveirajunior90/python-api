db_migration:
	alembic upgrade head

build:
	docker-compose up -d

run: db_migration
	python server.py