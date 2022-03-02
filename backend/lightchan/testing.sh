#!/bin/bash

PWD=pwd

rm -rf ./data
mkdir data
chmod 777 data
cd data
mkdir db
chmod 777 db
cd ..

docker-compose down
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker-compose build
docker-compose up 
