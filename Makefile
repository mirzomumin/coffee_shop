app:
	fastapi dev ./src/main.py

db:
	docker compose up -d

migration:
	alembic revision --autogenerate -m "$(message)"

migrate:
	alembic upgrade head
