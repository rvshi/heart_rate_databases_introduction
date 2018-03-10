from pymodm import connect
import models
import datetime


def add_heart_rate(input):
    message = ''
    code = 200
    return (message, code, None)


def get_hr(input):
    message = ''
    code = 200
    data = [233, 123]
    return (message, code, data)


def get_avg_hr(input):
    message = ''
    code = 200
    data = 2.3
    return (message, code, data)


def get_int_avg(input):
    message = ''
    code = 200
    data = 3.5
    return (message, code, data)


def add_heart_rate(email, heart_rate, time):
    # Get the first user where _id=suyash@suyashkumar.com
    user = models.User.objects.raw({"_id": "suyash@suyashkumar.com"}).first()
    # Append the heart_rate to the user's list of heart rates
    user.heart_rate.append(heart_rate)
    # append the current time to the user's list of heart rate times
    user.heart_rate_times.append(time)
    user.save()  # save the user to the database


def create_user():
    u = models.User("suyash@suyashkumar.com", 24, [],
                    [])  # create a new User instance
    u.heart_rate.append(60)  # add initial heart rate
    # add initial heart rate time
    u.heart_rate_times.append(datetime.datetime.now())
    u.save()  # save the user to the database


def print_user(email):
    # Get the first user where _id=suyash@suyashkumar.com
    user = models.User.objects.raw({"_id": "suyash@suyashkumar.com"}).first()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)


if __name__ == "__main__":
    # open up connection to db
    connect("mongodb://localhost:27017/heart_rate_app")
    # create_user() # we should only do this once, otherwise will overwrite
    # existing user
    add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    print_user("suyash@suyashkumar.com")
