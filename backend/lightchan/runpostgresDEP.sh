#!/bin/bash

postgresexists=0
while [ $postgresexists -lt 1 ]
do
        if [  "$(docker ps -qa -f name=dev-postgres)"  ]; then
		echo "dev-postgres exists creating database table..."
                echo "drop database if exists lightchan" | docker exec -i dev-postgres psql -U postgres
		echo "create database lightchan;" | docker exec -i dev-postgres psql -U postgres
		echo "drop user if exists pixel;" | docker exec -i dev-postgres psql -U postgres
		echo "create user pixel with encrypted password 'lightchan';" | docker exec -i dev-postgres psql -U postgres
		echo "grant all privileges on database lightchan to pixel;" | docker exec -i dev-postgres psql -U postgres
                postgresexists=1
	else
		echo "dev-postgres not yet instantiated"
                sleep 1
	fi
done 



