# Heart Rate Server with Database

[![Build Status](https://travis-ci.org/rvshi/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/rvshi/heart_rate_databases_introduction)

__Developed by:__ Harvey Shi (@rvshi)

__Course:__ BME 590 Spring 2018

A Python3 Flask server for heart rate data using a MongoDB database (running in a Docker container).

## API Usage
- `POST /api/heart_rate` to store heart rate measurements, using the following JSON format:
```
{
    "user_email": "me@harveyshi.com",
    "user_age": 100,
    "heart_rate": 82
}
```
    - where `user_age` is in years and `heart_rate` is in beats per minute
- `GET /api/heart_rate/<user_email>` will retrieve a list of the heart rate measurements for the specified user
- `GET /api/heart_rate/average/<user_email>` will return the average heart rate measurement for the specified user
- `POST /api/heart_rate/interval_average` will return the average heart rate for a user in the interval following a specified time, using the following JSON format:
  ```
  {
      "user_email": "me@harveyshi.com",
      "heart_rate_average_since": "2018-08-18T01:23:45.6789"
  }
  ```
    - __IMPORTANT:__ `heart_rate_average_since` must be in ISO 8601 format i.e. `YYYY-MM-DDTHH:MM:SS``
    - This will return a JSON with the average heart rate over the interval, as well as a boolean specifying if the average heart rate and specified age could indicate [tachycardia](https://en.wikipedia.org/wiki/Tachycardia), for example:
```
{
    "average": 77.23,
    "tachycardia": false
}
```
- All API responses include an `input` parameter echoing the request data, and a `message` parameter for logging information and error information for the request, for example:
```
{
    "data": 74.5,
    "input": "me@harveyshi.com",
    "message": "[INFO] avg. heart rate calculated for me@harveyshi.com."
}
```

## Installation
- First, set up the Python virtual environment and install all packages:
    ```bash
    $ virtualenv venv
    $ . venv/bin/activate
    $ sudo pip3 install -r requirements.txt
    ```
    - `sudo` is required for the `jsonschema` package
- [Install Docker](https://docs.docker.com/install) if it is not already installed, and run the following command:
docker pull mongo`
- Next, launch the database and server, in that order:
    ```bash
    $ ./run_db.sh
    $ ./run_server.sh
    ```
    - `run_server.sh` will attempt to run the server on port 80
    - if 80 is unavailable, you can change it
- Now, your server should be up and running!