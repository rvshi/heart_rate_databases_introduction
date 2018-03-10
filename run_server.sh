#!/bin/bash
sudo gunicorn --bind 0.0.0.0:8080 --workers 8 main:app
