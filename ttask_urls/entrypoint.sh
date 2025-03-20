#!/bin/sh

python manage.py migrate --no-input

pytest

python manage.py runserver