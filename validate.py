from jsonschema import validate, ValidationError
from dateformat import check_date

# Regex from http://emailregex.com
email_type = {
    'type': 'string',
    'pattern': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
}

heart_rate_type = {
    'type': 'object',
    'properties': {
        'user_email': email_type,
        'user_age': {
            'type': 'number',
            'minimum': 0
        },
        'heart_rate': {
            'type': 'integer',
            'minimum': 0,
            'maximum': 500
        }
    },
    'required': ['user_email', 'user_age', 'heart_rate'],
    'additionalProperties': False
}

interval_average_type = {
    'type': 'object',
    'properties': {
        'user_email': email_type,
        'heart_rate_average_since': {
            'type': 'string'
        }
    },
    'required': ['user_email', 'heart_rate_average_since'],
    'additionalProperties': False
}


def val_heart_rate(input):
    try:
        validate(input, heart_rate_type)
        return True
    except ValidationError:
        return False


def val_email(input):
    try:
        validate(input, email_type)
        return True
    except ValidationError:
        return False


def val_interval_average(input):
    try:
        validate(input, interval_average_type)
        return check_date(input['heart_rate_average_since'])
    except (ValueError, ValidationError):
        return False
