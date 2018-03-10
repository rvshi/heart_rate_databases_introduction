import datetime

ISO_8601 = '%Y-%m-%dT%H:%M:%S.%f'


def check_date(str):
    """ Checks if date string conforms to the ISO 8601 format

    :param str: string to check
    """
    try:
        datetime.datetime.strptime(str, ISO_8601)
        return True
    except ValueError as v:
        return False


def get_date(str):
    """ Parses date string in ISO 8601 format

    :param str: string to convert
    """
    return datetime.datetime.strptime(str, ISO_8601)


def get_str(d):
    """ Produces date string in ISO 8601 format

    :param str: datetime object to convert
    """
    return d.strftime(ISO_8601)
