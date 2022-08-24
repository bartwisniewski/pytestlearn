TEST_CONFIG = {'DB_URL': 'db1.company.com',
               'DB_USERNAME': 'user',
               'DB_PASSWORD': 'pass1234',
               'OK_MSG': 'connected',
               'NOK_MSG': 'connection error'}


def config(param):
    return TEST_CONFIG[param]

