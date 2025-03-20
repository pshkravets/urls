FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . .

ENTRYPOINT ["sh", "/app/entrypoint.sh"]

EXPOSE 8000

ENV DB_NAME=urls_db
ENV DB_PASSWORD=password
ENV DB_USER=postgres_user
ENV DB_HOST=db