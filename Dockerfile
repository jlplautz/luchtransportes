FROM python:3.11.1-slim

WORKDIR /app

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTCODE=1 \
    PIP_NO_CACHE_DIR=True \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false
ENV	PATH="$PATH:$POETRY_HOME/bin"

RUN pip install -U pip && pip install poetry
RUN apt update -y  && apt install -y --no-install-recommends -y\
    build-essential libpq-dev wait-for-it && apt clean && rm -rf /var/lib/apt/lists/*
# RUN curl -sSL https://install.python-poetry.org | python3 -

COPY . .

RUN poetry install

EXPOSE 8000

CMD [ "gunicorn", "--bind", ":8000", "backend.wsgi" ]