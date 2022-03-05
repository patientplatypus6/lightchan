#!/bin/bash

echo "inside entrypoint"
echo "deleting prior static images directory"
rm -rf ./static_images
echo "makemigrations"
python3 manage.py makemigrations
python3 manage.py makemigrations lightone
#python3 manage.py makemigrations lightchan
echo "migrate"
python3 manage.py migrate
python3 manage.py migrate lightone
#python3 manage.py migrate lightchan

#python3 manage.py collectstatic

echo "manage.py createsuperuser"
python3 manage.py createsuperuser \
  --noinput \
  --username pixel \
  --email peterweyand0@gmail.com
# --database lightchan

echo "now running the server"
#python3 manage.py runserver
daphne -b 0.0.0.0 -p 8000 lightchan.asgi:application
echo "now running the server"




