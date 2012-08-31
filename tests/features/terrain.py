from lettuce import *
import os
import shutil
import sys
import inspect
sys.path.append(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '../../eukalypse'))
from eukalypse import Eukalypse
from configobj import ConfigObj


@before.all
def setUpEnvironment():

    config = ConfigObj(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '../..', "tests/test.config"))

    world.CLEAN_TMP_DIR = config['clean_tmp_dir']  # cleanup after each test
    world.TMP_DIR = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '..', config['tmp_dir'])
    world.TEST_URL = config['test_url']

    if os.path.isdir(world.TMP_DIR):  # pragma: no cover
        shutil.rmtree(world.TMP_DIR)


@before.each_feature
def setUp(feature):
    if not os.path.isdir(world.TMP_DIR):
        os.mkdir(world.TMP_DIR)
    world.e = Eukalypse()
    world.e.resolution = (1280, 768)
    world.e.browser = 'chrome'
    world.e.output = world.TMP_DIR
    world.e.connect()


@after.each_feature
def tearDown(feature):
    world.e.disconnect()
    if world.CLEAN_TMP_DIR:
        shutil.rmtree(world.TMP_DIR)
