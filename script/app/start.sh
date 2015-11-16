#! /bin/bash

ENV_FILE=/tmp/olava-config/environment.sh

if [ -f $ENV_FILE ]; then
    echo "Loading configuration from $ENV_FILE"
    source $ENV_FILE
else
    echo "!WARNING! $ENV_FILE was not found"
fi

cd ./source
python main.py