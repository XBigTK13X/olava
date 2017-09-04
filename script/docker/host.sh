#! /bin/bash

docker run \
  --name olava \
  -v /tmp/olava-output/:/usr/share/nginx/html:ro \
  -p 40404:80 \
  -d nginx
