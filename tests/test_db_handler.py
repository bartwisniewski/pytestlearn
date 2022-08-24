import sys
import pytest

sys.modules['decouple'] = __import__('mock_decouple')

from mock_decouple import TEST_CONFIG
from functionality.db_handler import *


@pytest.fixture
def create_db_handler():
    db_handler = DbHandler()
    return db_handler


def test_connect_to_database(create_db_handler):
    db_url = TEST_CONFIG['DB_URL']
    username = TEST_CONFIG['DB_USERNAME']
    password = TEST_CONFIG['DB_PASSWORD']
    expected = f"I am connecting to {db_url} as {username} with pass: {password}..."

    actual = create_db_handler.connect_to_database()

    assert actual == expected


def test_show_msg_when_connected(create_db_handler):
    ok_msg = TEST_CONFIG['OK_MSG']
    expected = f"{ok_msg}"

    actual = create_db_handler.show_msg_when_connected()

    assert actual == expected


def test_show_msg_when_interrupted(create_db_handler):
    nok_msg = TEST_CONFIG['NOK_MSG']
    expected = f"{nok_msg}"

    actual = create_db_handler.show_msg_when_interrputed()

    assert actual == expected
