FROM python:3.9.5-slim-buster as base

COPY . .

RUN pip install flask
RUN pip install poetry
RUN poetry install

ENTRYPOINT poetry run flask run --host 0.0.0.0 --port 5000

EXPOSE 5000

# Configure for production
FROM base as production
ENTRYPOINT poetry run gunicorn -b 0.0.0.0:5000 app:app 

# Configure for local development
FROM base as development

ENTRYPOINT poetry run flask run --host 0.0.0.0 --port 5000
