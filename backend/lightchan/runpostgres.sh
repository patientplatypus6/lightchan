#!/bin/bash

		echo "dev-postgres exists creating database table..."
                echo "drop database if exists lightchan" | docker exec -i dev-postgres psql -U postgres
		echo "create database lightchan;" | docker exec -i dev-postgres psql -U postgres
		echo "drop user if exists pixel;" | docker exec -i dev-postgres psql -U postgres
		echo "create user pixel with encrypted password 'lightchan';" | docker exec -i dev-postgres psql -U postgres
		echo "grant all privileges on database lightchan to pixel;" | docker exec -i dev-postgres psql -U postgres
         
#docker exec -it -u root dev-postgres psql -h localhost -U postgres
#docker exec -it -u root dev-postgres psql -U postgres
#docker exec dev-postgres psql <<EOF 
#\l 
#EOF
#docker exec -it -u root dev-postgres postgres psql -h localhost -p 5432
#docker exec -it -u root dev-postgres postgres -U 
#docker exec -it -u root dev-postgres psql -h localhost -U postgres
#docker exec -it -u root dev-postgres create database lightchan;
#docker exec -it -u root dev-postgres create user pixel with encrypted password 'lightchan';
#docker exec -it -u root dev-postgres grant all privileges on database lightchan to pixel;
#docker exec -it -u root dev-postgres \q;
#docker exec -it -u root dev-postgres exit;


