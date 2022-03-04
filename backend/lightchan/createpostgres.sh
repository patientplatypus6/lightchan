#!/bin/bash


docker pull postgres

docker run -d \
        --name dev-postgres \
        -e POSTGRES_USERNAME=pixel \
        -e POSTGRES_PASSWORD=stardust \
        -v ${HOME}/postgres-data/:/var/lib/postgresql/data \
        -p 5432:5432 \
        postgres



