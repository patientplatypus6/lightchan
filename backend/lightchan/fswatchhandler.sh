#!/bin/bash

# fswatch -or ../../src | xargs -n1 -I{} echo "docker build --no-cache lightchan-frontend-1 && docker restart lightchan-frontend-1" | sudo docker exec --interactive lightchan-watchvolume-1 /bin/bash - 

# fswatch -or ../../src | xargs -n1 -I{} echo "docker-compose up -d --no-deps --build ligthchan-frontend-1" | sudo docker exec --interactive lightchan-watchvolume-1 /bin/bash - 


#!/bin/bash

# VAR1="Linuxize"
# VAR2="Linuxize"

# if [ "$VAR1" = "$VAR2" ]; then
#     echo "Strings are equal."
# else
#     echo "Strings are not equal."
# fi

# #!/bin/bash

# read -p "Enter first string: " VAR1
# read -p "Enter second string: " VAR2

# if [[ "$VAR1" == "$VAR2" ]]; then
#     echo "Strings are equal."
# else
#     echo "Strings are not equal."
# fi

# docker-compose up -d --no-deps --build <service_name>

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