#!/bin/bash

echo "inside entrypoint"
echo "deleting prior static images directory"
rm -rf ./static_images

# Do before sending data to backend
# echo "makemigrations"
# python3 manage.py makemigrations
# python3 manage.py makemigrations lightone

echo "migrate"
python3 manage.py migrate
python3 manage.py migrate lightone

echo "manage.py createsuperuser"
python3 manage.py createsuperuser \
  --noinput \
  --username pixel \
  --email peterweyand0@gmail.com
# --database lightchan

echo "now running the server"
daphne -b 0.0.0.0 -p 8000 lightchan.asgi:application
echo "now running the server"