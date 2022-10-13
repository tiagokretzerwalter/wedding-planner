FROM python:3.9-alpine3.16
LABEL maintainer="caneel"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
ARG COMPOSEDEBUG=false
RUN python -m venv /py
ENV PATH="/py/bin:$PATH"

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    if [ $COMPOSEDEBUG = "false" ]; \
        then rm -rf /tmp ; \
    fi && \
    apk --purge del .build-deps && \
    adduser \
        --disabled-password \
        django-user

USER django-user