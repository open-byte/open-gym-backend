FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /src

RUN apt-get update -y && apt-get install libpq5 -y

RUN pip install --upgrade pip

RUN pip install poetry

COPY ./pyproject.toml /src/pyproject.toml

RUN poetry config virtualenvs.create false

RUN poetry install --with dev

COPY ./src /src

EXPOSE 8000
