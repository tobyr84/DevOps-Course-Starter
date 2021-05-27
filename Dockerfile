FROM python:3.9.5-slim-buster

COPY . .

RUN pip install flask
RUN pip install poetry
RUN poetry install

ENTRYPOINT poetry run flask run --host 0.0.0.0 --port 5000

EXPOSE 5000

