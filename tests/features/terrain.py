from lettuce import *
import os
import shutil
import sys
import inspect
sys.path.append(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())),'../../eukalypse'))
from eukalypse import Eukalypse


@before.all
def setUpEnvironment():
	world.tmp_folder = os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '../assets/test_tmp')
	if os.path.isdir(world.tmp_folder): # pragma: no cover
		shutil.rmtree(world.tmp_folder)

@before.each_feature
def setUp(feature):
	if not os.path.isdir(world.tmp_folder):
		os.mkdir(world.tmp_folder)
	world.e = Eukalypse()
	world.e.resolution = (1280, 768)
	world.e.browser='chrome'
	world.e.output = world.tmp_folder
	world.e.connect()


@after.each_feature
def tearDown(feature):
	world.e.disconnect()
	#shutil.rmtree(world.tmp_folder)
