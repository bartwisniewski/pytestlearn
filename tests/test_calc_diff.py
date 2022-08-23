from datetime import datetime
import pytest
from functionality.calc_diff import calc_diff


def test_should_calc_diff_if_start_and_end_given():
    case = {
        'start_time': '2022-08-23T22:00:00+00:00',
        'end_time': '2022-08-23T22:00:10+00:00'
    }

    assert calc_diff(case) == 10


def test_should_calc_diff_if_longer_than_hour():
    case = {
        'start_time': '2022-08-23T22:00:00+00:00',
        'end_time': '2022-08-24T00:00:10+00:00'
    }

    assert calc_diff(case) == 7210


def test_should_return_negative_if_end_before_start():
    case = {
        'start_time': '2022-08-23T22:00:00+00:00',
        'end_time': '2022-08-23T21:59:30+00:00'
    }

    assert calc_diff(case) == -30


def test_should_return_zero_if_end_equals_start():
    case = {
        'start_time': '2022-08-23T22:00:00+00:00',
        'end_time': '2022-08-23T22:00:00+00:00'
    }

    assert calc_diff(case) == 0


@pytest.fixture
def set_datetime_mock(mocker):
    mock_datetime = mocker.patch('functionality.calc_diff.datetime')

    def mock_now(timezone):
        return datetime.fromisoformat('2022-08-23T22:00:30+00:00')

    def mock_fromisoformat(end_time):
        return datetime.fromisoformat(end_time)

    mocker.patch('functionality.calc_diff.datetime.fromisoformat', mock_fromisoformat)
    mocker.patch('functionality.calc_diff.datetime.now', mock_now)


def test_should_work_if_end_is_none(set_datetime_mock):
    case = {
        'start_time': '2022-08-23T22:00:00+00:00',
        'end_time': None
    }
    assert calc_diff(case) == 30
