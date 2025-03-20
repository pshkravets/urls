FROM python:3.11-slim-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip && pip install -r /usr/src/app/requirements.txt

COPY . .

ENV DB_NAME=urls_db
ENV DB_PASSWORD=password
ENV DB_USER=postgres_user
ENV DB_HOST=db
ENV DB_PORT=5432