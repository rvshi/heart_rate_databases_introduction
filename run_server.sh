#!/bin/bash
sudo gunicorn --bind 0.0.0.0:80 --workers 2 main:app
