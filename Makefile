install-requirements:
	pip install -r requirements.txt

run-api:
	uvicorn backend.src.server:app --reload
