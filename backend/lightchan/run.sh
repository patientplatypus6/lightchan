#!/bin/bash

echo "now pruning system"
docker system prune -f -a --volumes
echo "docker compose up --build"
docker compose up --build