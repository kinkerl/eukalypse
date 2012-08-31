from lettuce import *
import sys
import os


@step(u'I create a screenshot with the name "([^"]*)" of the url "([^"]*)"')
def create_screenshot(step, name, target_url):
    world.screenshot = world.e.screenshot(name, target_url)


@step(u'the screenshot response is not "([^"]*)"')
def screenshot_response_bool(step, bool_str):
    assert world.screenshot != (bool_str == 'True')


@step(u'the file "([^"]*)" exists')
def check_file_exists(step, filename):
    assert os.path.isfile(os.path.join(world.TMP_DIR, filename))


@step(u'I am connected to Selenium')
def check_connected_to_selenium(step):
    assert world.e.driver is not False


@step(u'I disconnect from Selenium')
def disconnect_from_selenium(step):
    world.e.disconnect()
    assert world.e.driver is None
