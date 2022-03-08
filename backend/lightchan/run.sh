#!/bin/bash

# daphne -e ssl:443:privateKey=./yourdomain.pem:certKey=./yourdomain_public.pem lightchan.asgi:application

# daphne -b 0.0.0.0 -p 8001 lightchan.asgi:application

# echo "now loading fswatch/backend on file changes"
# fswatch -or ../ | xargs -n1 -I{} docker restart backend   
# echo "now loading fswatch/frontend/src on file changes"
# fswatch -or ../../src | xargs -n1 -I{} docker restart frontend &
# echo "now starting node file"
# node ./watchfile.js

echo "docker compose down"
docker compose down --volumes
echo "docker compose build"
docker compose build 
echo "docker compose up"
docker compose up
