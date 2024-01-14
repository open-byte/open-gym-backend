FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install poetry

COPY ./pyproject.toml /app/pyproject.toml

RUN poetry config virtualenvs.create false

RUN poetry install --with dev

COPY ./app /app

EXPOSE 8000
