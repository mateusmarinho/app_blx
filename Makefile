install-requirements:
	pip install -r requirements.txt

run-api:
	uvicorn backend.src.server:app --reload --reload-dir=backend/src

init-alembic:
	alembic init alembic
