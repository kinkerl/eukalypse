from lettuce import *
import sys
import os
import inspect

sys.path.append(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())),'../../eukalypse'))
from eukalypse import Eukalypse
import shutil


@step('the test environment is created')
def environment_setup(step):
    world.tmp_folder = 'assets/test_tmp'
    #world.TESTURL = 'http://localhost:8400/'
    if os.path.isdir(world.tmp_folder): # pragma: no cover
        shutil.rmtree(world.tmp_folder)
    if not os.path.isdir(world.tmp_folder):
        os.mkdir(world.tmp_folder)

    
@step('the connection is established')
def connection_established(step):
    world.e = Eukalypse()
    world.e.resolution = (1280, 768)
    world.e.browser='chrome'
    world.e.output = world.tmp_folder
    world.e.connect()
    
@step('the connection is closed')
def connection_close(step):
    world.e.disconnect()
    
@step('the environment is cleaned')
def connection_close(step):
    shutil.rmtree(world.tmp_folder)

    
@step(u'I create a screenshot with the name "([^"]*)" of the url "([^"]*)"')

def create_screenshot(step, name, target_url):
    world.screenshot = world.e.screenshot(name, target_url)
    
@step(u'the screenshot response is not "([^"]*)"')
def screenshot_response_bool(step, bool_str):
    assert world.screenshot != (bool_str == 'True')
    
@step(u'the file "([^"]*)" exists')
def check_file_exists(step, filename):
    os.path.isfile(os.path.join(world.tmp_folder, filename))
    

