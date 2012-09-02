#import unittest
import os
import shutil
from configobj import ConfigObj

config = ConfigObj("test.config")

CLEAN_TMP_DIR = config['clean_tmp_dir']
TEST_URL = config['test_url']
TMP_DIR = config['tmp_dir']


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    if CLEAN_TMP_DIR and os.path.isdir(TMP_DIR):  # pragma: no cover
        shutil.rmtree(TMP_DIR)
    if not os.path.isdir(TMP_DIR):
        os.mkdir(TMP_DIR)


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module method. """
    if CLEAN_TMP_DIR:
        shutil.rmtree(TMP_DIR)


def test_reconnect(eukalypse):
    assert eukalypse.driver is not False
    eukalypse.connect()
    assert eukalypse.driver is not False


def test_disconnect(eukalypse):
    assert eukalypse.driver is not False
    eukalypse.disconnect()
    assert eukalypse.driver is None


def test_screenshot(eukalypse, test_url):
    """
    Just try to create a screenshot
    """
    screenshot = eukalypse.screenshot('test_screenshot', test_url)
    assert screenshot is not False
    assert os.path.isfile(screenshot)


def test_screenshot_connect(eukalypse, test_url):
    """
    Try to create a screenshot and test the auto-connect function
    if eukalypse is not connected to the selenium server.
    """
    assert eukalypse.driver is not False
    eukalypse.disconnect()
    assert eukalypse.driver is None
    screenshot = eukalypse.screenshot('test_screenshot_connect', test_url)
    assert screenshot is not False
    assert os.path.isfile(screenshot)


def test_compareClean(eukalypse, test_url):
    """
    Match against a clean screenshot and expect no error.
    """
    response = eukalypse.compare('test_compareClean', 'assets/reference_test_screenshot.png', test_url)
    _response_clean(response)


def test_compareCleanSmallReference(eukalypse, test_url):
    response = eukalypse.compare('test_compareCleanSmallReference', 'assets/reference_test_screenshot_tosmall.png', test_url)
    _response_clean(response)


def test_compareCleanLargeReference(eukalypse, test_url):
    response = eukalypse.compare('test_compareCleanLargeReference', 'assets/reference_test_screenshot_tolarge.png', test_url)
    _response_clean(response)


def test_compareCleanLargeReferenceTainted(eukalypse, test_url):
    response = eukalypse.compare('test_compareCleanLargeReferenceTainted', 'assets/reference_test_screenshot_tolarge2.png', test_url)
    _response_clean(response)


def test_compareCleanLargeReferenceTainted2(eukalypse, test_url):
    response = eukalypse.compare('test_compareCleanLargeReferenceTainted2', 'assets/reference_test_screenshot_tolarge3.png', test_url)
    _response_tainted(response)


def test_compareTainted(eukalypse, test_url):
    """
    Match against a tainted screenshot and get the error.
    """
    response = eukalypse.compare('test_compareTainted', 'assets/reference_test_screenshot_tainted.png', test_url)
    _response_tainted(response)


def test_compareTaintedMask(eukalypse, test_url):
    """
    Match against a tainted screenshot but use a ignore mask to
    cut out the expected error.
    """
    response = eukalypse.compare('test_compareTaintedMask', 'assets/reference_test_screenshot_tainted.png', test_url, 'assets/reference_test_screenshot_tainted_mask.png')
    _response_clean(response)


def test_compareTaintedMask2(eukalypse, test_url):
    """
    Match with a "wrong" irgnore mask and expect a tainted error
    """
    response = eukalypse.compare('test_compareTaintedMask2', 'assets/reference_test_screenshot_tainted.png', test_url, 'assets/reference_test_screenshot_tainted_mask2.png')
    _response_tainted(response)


def test_compareTaintedMask3(eukalypse, test_url):
    response = eukalypse.compare('test_compareTaintedMask3', 'assets/reference_test_screenshot_tainted.png', test_url, 'assets/reference_test_screenshot_tainted_mask_stretch.png')
    _response_clean(response)


def test_compareTaintedMask4(eukalypse, test_url):
    response = eukalypse.compare('test_compareTaintedMask4', 'assets/reference_test_screenshot_tainted.png', test_url, 'assets/reference_test_screenshot_tainted_mask_stretch2.png')
    _response_clean(response)


def test_compareTaintedMask5(eukalypse, test_url):
    response = eukalypse.compare('test_compareTaintedMask5', 'assets/reference_test_screenshot_tainted.png', test_url, 'assets/reference_test_screenshot_tainted_mask_stretch3.png')
    _response_tainted(response)


def test_execute(eukalypse, test_url):
    """
    Test execution of selenium statements
    """
    statement = """
driver = self.driver
driver.get(self.base_url + "/")
driver.set_window_size(1280, 768)
driver.find_element_by_id("clickme").click()
    """
    eukalypse.base_url = test_url
    eukalypse.execute(statement)
    response = eukalypse.compare('execute', 'assets/reference_test_screenshot_index2.png')
    _response_clean(response)


def test_execute_row(eukalypse, test_url):
    """
    Test multiple execution of selenium statements and compare 2
    screenshots to verify the progress of the execution.
    """
    statement = """
driver = self.driver
driver.get(self.base_url + "/")
driver.set_window_size(1280, 768)
driver.find_element_by_css_selector('input[type="text"]').clear()
driver.find_element_by_css_selector('input[type="text"]').send_keys("asd")
    """

    eukalypse.base_url = test_url
    eukalypse.execute(statement)
    response = eukalypse.compare('execute_row1', 'assets/reference_test_screenshot_input.png')
    _response_clean(response)

    statement = """
driver = self.driver
driver.find_element_by_css_selector('input[type="submit"]').click()
    """

    eukalypse.execute(statement)
    response = eukalypse.compare('execute_row2', 'assets/reference_test_screenshot_index2.png')
    _response_clean(response)


def _response_clean(response):
    """
    Helper function to check if a response object is clean and
    the attributes looks clean.
    """
    assert response.clean
    assert response.identifier != ''
    assert response.dirtiness is 0

    assert response.target_url != ''

    assert response.target_img != ''
    assert os.path.isfile(response.target_img)

    assert response.reference_img != ''
    assert os.path.isfile(response.reference_img)

    assert response.difference_img == ''
    assert not os.path.isfile(response.difference_img)

    assert response.difference_img_improved == ''
    assert not os.path.isfile(response.difference_img_improved)


def _response_tainted(response):
    """
    Helper function to check if a response object is tainted,
    the attributes look tainted and the difference images are created.
    """
    assert not response.clean
    assert response.identifier != ''
    assert response.dirtiness != 0
    assert response.target_url != ''

    assert response.target_img != ''
    assert os.path.isfile(response.target_img)

    assert response.reference_img != ''
    assert os.path.isfile(response.reference_img)

    assert response.difference_img != ''
    assert os.path.isfile(response.difference_img)

    assert response.difference_img_improved != ''
    assert os.path.isfile(response.difference_img_improved)
