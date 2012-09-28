from lettuce import *
import os
import shutil
import inspect
from eukalypse.eukalypse import Eukalypse
import ConfigParser




@before.all
def setUpEnvironment():
    config = ConfigParser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "..", "config.cfg"))

    world.CLEAN_TMP_DIR = config.get('main', 'clean_tmp_dir')  # cleanup after each test
    world.TMP_DIR = os.path.join(os.path.dirname(__file__), '..', config.get('main', 'tmp_dir'))
    world.TEST_URL = config.get('main', 'test_url')

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
