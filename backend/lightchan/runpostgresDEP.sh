#!/bin/bash


#docker pull postgres

#docker run -d \
#	--name dev-postgres \
#	-e POSTGRES_USERNAME=pixel \
#	-e POSTGRES_PASSWORD=stardust \
#	-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
#        -p 5432:5432 \
#        postgres

#docker exec -u root -t -i dev-postgres bash <<'EOF'
#echo 'hello'
#psql -h localhost -U postgres
#psql postgres
#create database lightchan;
#create user pixel with encrypted password 'lightchan';
#grant all privileges on database lightchan to pixel;
#\q
#exit
#EOF
#EOF

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


