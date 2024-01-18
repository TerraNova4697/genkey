FROM python:3.11-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./requirements /tmp/requirements
COPY . /app
WORKDIR /app
EXPOSE 5000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual \
        postgresql-dev musl-dev libpq-dev gcc && \
    /py/bin/pip install -r /tmp/requirements/dev.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        flask-user

ENV PATH="/py/bin:$PATH"

USER flask-user
