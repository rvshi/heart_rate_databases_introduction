# Heart Rate Server with Database

[![Build Status](https://travis-ci.org/rvshi/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/rvshi/heart_rate_databases_introduction)

__Developed by:__ Harvey Shi (@rvshi)

__Course:__ BME 590 Spring 2018

A Flask server for heart rate data using a MongoDB database (running in a Docker container).

## API Endpoints
- `POST /api/heart_rate` to store heart rate measurements, using the following json format:
  ```
  {
      "user_email": "me@harveyshi.com",
      "user_age": 100,
      "heart_rate": 82
  }
  ```
    - `user_age` is in years
    - `heart_rate` is in beats per minute
- `GET /api/heart_rate/<user_email>` will retrieve the heart rate measurements for the specified user
- `GET /api/heart_rate/average/<user_email>` will return the average heart rate measurement for the specified user
- `POST /api/heart_rate/interval_average` will return the average heart rate for a user over after a specific time, using the following json format:
  ```
  {
      "user_email": "me@harveyshi.com",
      "heart_rate_average_since": "2018-08-18T01:23:45.6789"
  }
  ```
    - `heart_rate_average_since` must be in ISO 8601 format i.e. `YYYY-MM-DDTHH:MM:SS`