"""Database setup and basic functions
"""
from pymodm import connect, errors
import models
import datetime
from dateformat import get_date

mongo_url = 'mongodb://localhost:27017/heart_rate_app'
connect(mongo_url)


def add_heart_rate(input):
    return (update_user(**input), None, 200)


def get_hr(user_email):
    try:
        u = models.User.objects.raw({'_id': user_email}).first()
        message = '[INFO] heart rate data retrieved for {}.'.format(
            user_email)
        data = []
        for i, time in enumerate(u.heart_rate_times):
            data.append([time,u.heart_rate[i]])
        return (message, data, 200)
    except errors.DoesNotExist:
        return('[ERROR] user not found', None, 400)


def get_avg_hr(user_email):
    try:
        u = models.User.objects.raw({'_id': user_email}).first()
        message = '[INFO] avg. heart rate calculated for {}.'.format(
            user_email)
        return (message, calc_avg(u.heart_rate), 200)
    except errors.DoesNotExist:
        return('[ERROR] user not found', None, 400)


def get_int_avg(input):
    user_email = input['user_email']
    date_string = get_date(input['heart_rate_average_since'])

    try:
        u = models.User.objects.raw({'_id': user_email}).first()
        message = '[INFO] avg. heart rate calculated for {} after {}.'.format(
            user_email, input['heart_rate_average_since'])

        # determine heart rates in interval
        heart_rates = []
        for i, time in enumerate(u.heart_rate_times):
            if(time > date_string):
                heart_rates.append(u.heart_rate[i])

        if(len(heart_rates) > 0):
            avg = calc_avg(heart_rates)
            data = {
                'average': avg,
                'tachycardia': has_tachycardia(u.age, avg)
            }
            return(message, data, 200)
        else:
            return('[ERROR] no data for specified interval', None, 400)
    except errors.DoesNotExist:
        return('[ERROR] user not found', None, 400)


def calc_avg(l):
    return sum(l) / float(len(l))


def has_tachycardia(age, hr):
    t0 = age < 1 and hr > 169
    t1 = (1 <= age and age < 3) and hr > 151
    t2 = (3 <= age and age < 5) and hr > 137
    t3 = (5 <= age and age < 8) and hr > 133
    t4 = (8 <= age and age < 12) and hr > 130
    t5 = (12 <= age and age < 15) and hr > 119
    t6 = age >= 15 and hr > 100
    return any([t0, t1, t2, t3, t4, t5, t6])


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
        message = '[INFO] Added heart rate entry for {}.'.format(user_email)
    user.save()
    return message


def print_user(email):
    try:
        user = models.User.objects.raw({'_id': email}).first()
        print('\nUser: {}'.format(user.email))
        print('Age:  {}'.format(user.age))
        print(user.heart_rate)
        print(user.heart_rate_times)
    except errors.DoesNotExist:
        print('User not found')


def delete_user(email):
    try:
        user = models.User.objects.raw({'_id': email}).first()
        user.delete()
        message = '[INFO] Deleted user {}.'.format(email)
        print(message)
    except errors.DoesNotExist:
        print('User not found')
