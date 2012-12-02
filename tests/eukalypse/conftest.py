from eukalypse import Eukalypse
import ConfigParser
import os
from mock import MagicMock

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.cfg"))


TEST_URL = config.get('main', 'test_url')
TMP_DIR = config.get('main', 'tmp_dir')


class Remote:
    """
    A Mock implementation of a selenium driver.
    This is only used for internal unit testing and is strongly tied to these tests.
    It replaced the calls to selenium and returns pre-genereated screenshots.
    The overwrite attribute handels different images responses for some tests.
    """

    def __init__(self):
        self.overwrite = None
        pass

    def connect(self):
        """nothing to do here"""
        pass

    def close(self):
        """nothing to do here"""
        pass

    def set_window_size(self, width, height):
        """nothing to do here"""
        pass

    def get(self, url=None):
        pass

    def get_screenshot_as_file(self, destination):
        if self.overwrite:
            tmp = self.overwrite
            self.overwrite = None
            return tmp
        return "tests/assets/reference_test_screenshot.png"

    def find_element_by_id(self, id):
        if id == 'clickme':  #te used in test_execute_selenium
            self.overwrite = 'tests/assets/reference_test_screenshot_index2.png'
        return MagicMock()

    def find_element_by_css_selector(self, selector):
        if selector == 'input[type="text"]':  # used in test_execute_row_selenium
            self.overwrite = 'tests/assets/reference_test_screenshot_input.png'
        elif selector == 'input[type="submit"]':  # used in test_execute_row_selenium
            self.overwrite = 'tests/assets/reference_test_screenshot_index2.png'
        return MagicMock()


def connect(instance):
    """Helper mock function to overwrite the eukalypse connect function.
    This function does NOT connect to selenium but ties eukalypse to a selenium mock object"""
    instance.driver = Remote()


def pytest_funcarg__eukalypse(request):
    import os
    print os.path.realpath(__file__)
    eukalypse = Eukalypse()
    eukalypse.resolution = (1280, 768)
    eukalypse.browser = 'chrome'
    eukalypse.output = TMP_DIR

    #monkeypatch the Eukalypse object tp NOT use selenium but our own mock class
    funcType = type(Eukalypse.connect)
    eukalypse.connect = funcType(connect, eukalypse, Eukalypse)

    eukalypse.connect()

    def eukalypse_teardown():
        eukalypse.disconnect()

    request.addfinalizer(eukalypse_teardown)
    return eukalypse


def pytest_funcarg__test_url(request):
    return TEST_URL
