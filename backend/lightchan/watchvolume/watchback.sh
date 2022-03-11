#!/bin/bash

fswatch -or ../../lightone/*.py ../../lightchan/*.py ../../media ../../static | xargs -n1 -I{} docker restart lightchan-backend-1