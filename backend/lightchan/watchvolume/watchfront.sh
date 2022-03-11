#!/bin/bash

fswatch -or ../../../src ../../../public | xargs -n1 -I{} docker restart lightchan-frontend-1