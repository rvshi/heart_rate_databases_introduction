"""Database setup and basic functions
"""
from pymodm import connect, errors
import models
import datetime

mongo_url = 'mongodb://localhost:27017/heart_rate_app'
connect(mongo_url)


def add_heart_rate(input):
    message = update_user(**input)
    code = 200
    return (message, None, code)


def get_hr(user_email):
    try:
        u = models.User.objects.raw({'_id': user_email}).first()
        message = '[INFO] heart rate data retrieved for {}.'.format(
            user_email)
        data = u.heart_rate
        return (message, data, 200)
    except errors.DoesNotExist:
        message = '[ERROR] user not found'
        return(message, None, 400)


def get_avg_hr(user_email):
    message = ''
    data = 2.3
    return (message, data, 200)


def get_int_avg(input):
    message = ''
    data = 3.5
    return (message, data, 200)


def update_user(user_email, user_age, heart_rate):
    time_stamp = datetime.datetime.now()

    query_set = models.User.objects.raw({'_id': user_email})
    if(query_set.count() == 0):
        user = models.User(user_email, user_age, [heart_rate], [time_stamp])
        message = '[INFO] Created new user and added heart rate entry.'
    else:
        user = query_set.first()
        user.age = user_age
        user.heart_rate.append(heart_rate)
        user.heart_rate_times.append(time_stamp)
        message = '[INFO] Added heart rate entry.'
    user.save()
    return message


def print_user(email):
    try:
        user = models.User.objects.raw({'_id': email}).first()
        print(user.email)
        print(user.age)
        print(user.heart_rate)
        print(user.heart_rate_times)
    except errors.DoesNotExist:
        print('User not found')


def delete_user(email):
    try:
        user = models.User.objects.raw({'_id': email}).first()
        user.delete()
    except errors.DoesNotExist:
        print('User not found')


if __name__ == '__main__':
    email = 'me@harveyshi.com'
    example_user = {'user_email': email,
                    'user_age': 100,
                    'heart_rate': 82
                    }

    print(update_user(**example_user))
    print(get_hr(email))
    print_user(email)
    delete_user(email)
