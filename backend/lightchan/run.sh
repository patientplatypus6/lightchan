#!/bin/bash

# daphne -e ssl:443:privateKey=./yourdomain.pem:certKey=./yourdomain_public.pem lightchan.asgi:application

# daphne -b 0.0.0.0 -p 8001 lightchan.asgi:application

# echo "now loading fswatch/backend on file changes"
# fswatch -or ../ | xargs -n1 -I{} docker restart backend   
# echo "now loading fswatch/frontend/src on file changes"
# fswatch -or ../../src | xargs -n1 -I{} docker restart frontend &
# echo "now starting node file"
# node ./watchfile.js

# rm -rf data
# mkdir data && chmod 777 data && cd data && mkdir db & chmod 777 && ../..

# cd ./watchvolume
# ./watchfront.sh &
# ./watchback.sh &
# cd ..

# ≈   
# fswatch -or ../../src | xargs -n1 -I{} docker restart frontend

echo "now deleting prior db instantiation"

# rm -rf data
# mkdir data
# cd data
# mkdir db 
# chmod 777 db
# cd ..
# chmod 777 data

echo "now pruning system"
docker system prune -f -a --volumes
echo "docker compose down"
docker compose down --volumes
echo "docker compose build"
docker compose build 
echo "docker compose up -d --build"
docker compose up