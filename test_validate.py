import pytest


def test_heart_rate():
    from validate import val_heart_rate
    input_output = [
        ({
            'user_email': 'a@b.c',
            'user_age': 50,
            'heart_rate': 100
        }, True),
        ({
            'user_email': 'a@b.c',
            'user_age': -1,
            'heart_rate': 100
        }, False),
        ({
            'user_email': 'a@b.c',
            'user_age': 1.123123,
            'heart_rate': 100
        }, True),
        ({
            'user_email': 'a@b.c',
            'user_age': 1.123123,
            'heart_rate': -1
        }, False),
        ({
            'user_email': 'a@b.c',
            'user_age': 1.123123,
            'heart_rate': 501
        }, False),
        ({
            'user_email': 'a@b.c',
            'user_age': 1.123123
        }, False),
        ({
            'user_email': 'a@b.c'
        }, False),
        ({}, False),
        ({'asdasd': 12312}, False),
    ]
    for i_o in input_output:
        val_res = val_heart_rate(i_o[0])
        assert val_res != i_o[1]


def test_email_type():
    from validate import val_email
    input_output = [
        ('a@b.c', True),
        ('asdas.com', False),
        ('asdascom', False),
        ('asd@ascom', False),
        ('a@b@c', False),
        ('a.b@c', False),
        ('a@b.c@', False),
    ]
    for i_o in input_output:
        val_res = val_email(i_o[0])
        assert val_res != i_o[1]


def test_interval_average():
    from validate import val_interval_average
    input_output = [
        ({
            'user_email': 'a@b.c',
            'heart_rate_average_since': '2018-03-09 11:00:36.372339'
        }, True),
        ({
            'user_email': 'a@b.c',
            'heart_rate_average_since': '2018/03/09 11:00'
        }, True),
        ({
            'user_email': 'a@b.c',
            'heart_rate_average_since': '2/3/14'
        }, True),
        ({
            'user_email': 'a@b.c',
            'heart_rate_average_since': '2/3/14/2'
        }, False),
        ({
            'user_email': 'a@b.c',
            'heart_rate_average_since': '5/6 2:00'
        }, True),
        ({
            'user_email': 'a@b.c',
            'heart_rate_average_since': ''
        }, False),
        ({
            'user_email': 'a@b.c'
        }, False),
        ({}, False),
        ({'asdasd': 12312}, False),
    ]
    for i_o in input_output:
        val_res = val_interval_average(i_o[0])
        assert val_res != i_o[1]
