#!/bin/bash
docker run -v $PWD/db:/data/db -p 127.0.0.1:27017:27017 mongo