#!/bin/bash

echo ^^^^^^^^^^^^^^^^
echo STOPPING LOCAL POSTGRESQL SERVICE
service postgresql stop
echo ^^^^^^^^^^^^^^^^
echo CLEANING DOCKER
./dockerclean.sh
echo ^^^^^^^^^^^^^^^^
echo RUNNING POSTGRES DOCKER
./runpostgres.sh
echo ^^^^^^^^^^^^^^^^
echo RUN DOCKER BACKEND
sudo docker build . -t lightchanbackend --network=host
sudo docker run -d -p 127.0.0.1:8001:8001/tcp lightchanbackend
echo ^^^^^^^^^^^^^^^^
echo SPIN APPLICATION
echo ./run.sh
echo ^^^^^^^^^^^^^^^^

