from configobj import ConfigObj
from eukalypse.eukalypse import Eukalypse

config = ConfigObj("test.config")


TEST_URL = config['test_url']
TMP_DIR = config['tmp_dir']


def pytest_funcarg__eukalypse(request):

    eukalypse = Eukalypse()
    eukalypse.resolution = (1280, 768)
    eukalypse.browser = 'chrome'
    eukalypse.output = TMP_DIR
    eukalypse.connect()

    def eukalypse_teardown():
        eukalypse.disconnect()

    request.addfinalizer(eukalypse_teardown)
    return eukalypse


def pytest_funcarg__test_url(request):
    return TEST_URL
