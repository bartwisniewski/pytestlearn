import pytest
from functionality.db_handler import DbHandler
TEST_CONFIG = {'DB_URL': 'db1.company.com',
               'DB_USERNAME': 'user',
               'DB_PASSWORD': 'pass1234',
               'OK_MSG': 'connected',
               'NOK_MSG': 'connection error'}


@pytest.fixture
def set_config_mock(mocker):

    class MyConfig:
        DB_URL: str = TEST_CONFIG['DB_URL']
        DB_USERNAME: str = TEST_CONFIG['DB_USERNAME']
        DB_PASSWORD: str = TEST_CONFIG['DB_PASSWORD']
        OK_MSG: str = TEST_CONFIG['OK_MSG']
        NOK_MSG: str = TEST_CONFIG['NOK_MSG']

    # def my_config(param: str) -> str:
    #    return TEST_CONFIG.get(param)

    mocker.patch('functionality.db_handler.Config', MyConfig)
    # mocker.patch('functionality.db_handler.config', my_config)


@pytest.fixture
def create_db_handler(set_config_mock):

    return DbHandler()


def test_should_connect_to_database(create_db_handler):

    db_url = TEST_CONFIG['DB_URL']
    username = TEST_CONFIG['DB_USERNAME']
    password = TEST_CONFIG['DB_PASSWORD']
    expected = f"I am connecting to {db_url} as {username} with pass: {password}..."

    actual = create_db_handler.connect_to_database()

    assert actual == expected


def test_should_show_msg_when_connected(create_db_handler):
    ok_msg = TEST_CONFIG['OK_MSG']
    expected = f"{ok_msg}"

    actual = create_db_handler.show_msg_when_connected()

    assert actual == expected


def test_should_show_msg_when_interrupted(create_db_handler):
    nok_msg = TEST_CONFIG['NOK_MSG']
    expected = f"{nok_msg}"
    from functionality.db_handler import DbHandler
    actual = create_db_handler.show_msg_when_interrputed()

    assert actual == expected
