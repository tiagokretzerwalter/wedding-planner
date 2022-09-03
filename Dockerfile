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
RUN python -m venv /py
ENV PATH="/py/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user