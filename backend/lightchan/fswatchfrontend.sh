#!/bin/bash

fswatch -or ../../src | xargs -n1 -I{} echo "docker restart lightchan-frontend-1" | sudo docker exec --interactive lightchan-watchvolume-1 /bin/bash - 

echo "should never reach here"