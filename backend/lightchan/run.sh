#!/bin/bash

# daphne -e ssl:443:privateKey=./yourdomain.pem:certKey=./yourdomain_public.pem lightchan.asgi:application

ls

daphne -b 0.0.0.0 -p 8001 lightchan.asgi:application


