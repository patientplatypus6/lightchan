#!/bin/bash

fswatch --batch-marker=EOF -xn ../.. | while read file event; do 
   echo $file $event
   if [[ $file == *"data/db"* ]]; then
        echo "do nothing data/db changed"
   elif [[ $file == *"__pycache__"* ]]; then
        echo "do nothing __pycache__ changed"
   elif [[ $file == *"migrations"* ]]; then
        echo "do nothing migrations changed"
   elif [[ $file == *"env"* ]]; then
        echo "do nothing env changed"
   elif [[ $file == *"backend"* ]]; then
        echo "backend changed now re-upping"
        docker-compose up --detach --build backend
   elif [[ $file == *"src"* ]]; then
        echo "src changed now re-upping"
        docker-compose up --detach --build frontend
   fi
done

echo "should never reach here"