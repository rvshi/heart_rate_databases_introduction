import pytest


def test_calc_avg():
    from database import calc_avg
    input_output = [
        ([1], 1),
        ([2, 3, 4], 3),
        ([1, 0, -1], 0),
        ([12, 3, 3, 4, 3, 2], 4.5),
        ([100000001, 1], 50000001)
    ]
    for i_o in input_output:
        assert pytest.approx(i_o[1], calc_avg(i_o[0]))


def test_has_tachycardia():
    from database import has_tachycardia
    input_output = [
        (0, 170, True),
        (0, 168, False),
        (1, 152, True),
        (1, 151, False),
        (3, 138, True),
        (3, 137, False),
        (5, 134, True),
        (5, 133, False),
        (8, 131, True),
        (8, 130, False)
    ]
    for i_o in input_output:
        assert i_o[2] == has_tachycardia(i_o[0], i_o[1])
