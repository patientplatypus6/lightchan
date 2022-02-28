#!/bin/bash

systemctl restart docker

docker image prune -f

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune --volumes -f

