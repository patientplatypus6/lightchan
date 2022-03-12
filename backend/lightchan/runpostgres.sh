#!/bin/bash

		echo "dev-postgres exists creating database table..."
                echo "drop database if exists lightchan" | docker exec -i dev-postgres psql -U postgres
		echo "create database lightchan;" | docker exec -i dev-postgres psql -U postgres
		echo "drop user if exists pixel;" | docker exec -i dev-postgres psql -U postgres
		echo "create user pixel with encrypted password 'lightchan';" | docker exec -i dev-postgres psql -U postgres
		echo "grant all privileges on database lightchan to pixel;" | docker exec -i dev-postgres psql -U postgres
         

