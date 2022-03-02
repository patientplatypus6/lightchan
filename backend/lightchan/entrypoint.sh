#!/bin/bash


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser \
  --noinput \
  --username pixel \
  --email peterweyand0@gmail.com
# --database lightchan



