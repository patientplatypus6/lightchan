#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE lightchan;
EOSQL

#docker exec -it -u root dev-postgres postgres psql -h localhost -p 5432
