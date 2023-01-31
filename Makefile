create-env:
	python3 -m venv venv; source venv/bin/activate

install-requirements:
	pip install -r requirements.txt

run-api:
	uvicorn backend.src.server:app --reload
