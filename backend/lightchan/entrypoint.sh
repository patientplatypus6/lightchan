#!/bin/bash


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser \
  --noinput \
  --username pixel \
  --email peterweyand0@gmail.com
# --database lightchan

echo "now running the server"
# python3 manage.py runserver
daphne -b 0.0.0.0 -p 8000 lightchan.asgi:application
echo "now running the server"
