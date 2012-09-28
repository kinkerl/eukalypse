from eukalypse.eukalypse import Eukalypse
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.cfg"))


TEST_URL = config.get('main', 'test_url')
TMP_DIR = config.get('main', 'tmp_dir')


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
