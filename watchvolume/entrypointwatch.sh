#!/bin/bash

echo "inside the entrypoint.sh file for watchvolume"
echo 'first ls'
ls
echo "cd .."
cd ..
echo "second ls"
ls  

function restart_frontend() {
    docker restart lightchan-frontend-1
}

function restart_backend() {
    docker restart lightchan-backend-1
}

# STR='GNU/Linux is an operating system'
# SUB='Linux'
# if [[ "$STR" == *"$SUB"* ]]; then
#   echo "It's there."
# fi

# inotifywait -m -r /code --format '%w%f' -e create -e delete -e modify -e moved_to | 
# while read dir action file; do
#     echo "File ${file} action ${action} directory ${dir}"
# done

function keep_alive() {
    echo "inside keep alive for watchvolume"
    sleep 5000
    keep_alive
}

keep_alive