import pytest


@pytest.mark.skip(reason="requires docker instance")
def test_database():
    import database
    import datetime
    from time import sleep
    from dateformat import get_str

    email = 'a@b.c'
    e1 = {'user_email': email,
          'user_age': 100,
          'heart_rate': 82
          }
    e2 = {'user_email': email,
          'user_age': 101,
          'heart_rate': 45
          }

    print(database.update_user(**e1))
    database.print_user(email)

    print(database.update_user(**e2))
    database.print_user(email)

    new_time = get_str(datetime.datetime.now())
    print(new_time)

    int_avg = {
        'user_email': 'a@b.c',
        'heart_rate_average_since': new_time
    }
    print(database.get_int_avg(int_avg))
    database.delete_user(email)


if __name__ == '__main__':
    test_database()
