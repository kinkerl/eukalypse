"""
This is a helper script to generate new reference images on a new system.
These reference images are only used for internal unit testing.
"""
import sys
import os
import inspect
sys.path.append(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '../eukalypse'))
from eukalypse import Eukalypse
from PIL import Image
import ImageDraw
import logging as logger
logger.basicConfig(level=logger.INFO)


tmp_folder = 'tests/assets'
e = Eukalypse()
e.resolution = (1280, 768)
e.browser = 'chrome'
e.output = tmp_folder
e.connect()
logger.info("getting first screenshot")
screenshot = e.screenshot('reference_test_screenshot', 'http://localhost:8400/index.html')
logger.info("writing reference_test_screenshot.png")
logger.info("getting second screenshot")
screenshot = e.screenshot('reference_test_screenshot_index2', 'http://localhost:8400/index2.html')
logger.info("writing reference_test_screenshot_index2.png")

statement = """
driver = self.driver
driver.get("http://localhost:8400/index.html")
driver.set_window_size(1280, 768)
driver.find_element_by_css_selector('input[type="text"]').clear()
driver.find_element_by_css_selector('input[type="text"]').send_keys("asd")
"""
e.execute(statement)
e.screenshot('reference_test_screenshot_input')
e.disconnect()

CLEANBASE_FILENAME = os.path.join(tmp_folder, "reference_test_screenshot.png")

im = Image.open(CLEANBASE_FILENAME)
draw = ImageDraw.Draw(im)
draw.rectangle((10, 10, 100, 30), fill="red")
del draw

# write to stdout
OUTPUTFILENAME = "reference_test_screenshot_tainted.png"
logger.info("writing {0}".format(OUTPUTFILENAME))
im.save(os.path.join(tmp_folder, OUTPUTFILENAME), "PNG")


# 3 large
im = Image.open(CLEANBASE_FILENAME)
im_size = im.size
largeimage = Image.new('RGB', (1600, 900), (255, 255, 255))
largeimage.paste(im, (0, 0, im_size[0], im_size[1]))

OUTPUTFILENAME = "reference_test_screenshot_tolarge.png"
logger.info("writing {0}".format(OUTPUTFILENAME))
largeimage.save(os.path.join(tmp_folder, OUTPUTFILENAME), "PNG")

#
im = Image.open(CLEANBASE_FILENAME)
im_size = im.size
largeimage = Image.new('RGB', (1600, 900), (255, 255, 255))
largeimage.paste(im, (0, 0, im_size[0], im_size[1]))

draw = ImageDraw.Draw(largeimage)
draw.rectangle((1550, 850, 1600, 900), fill="red")
del draw

OUTPUTFILENAME = "reference_test_screenshot_tolarge2.png"
logger.info("writing {0}".format(OUTPUTFILENAME))
largeimage.save(os.path.join(tmp_folder, OUTPUTFILENAME), "PNG")

im = Image.open(CLEANBASE_FILENAME)
im_size = im.size
largeimage = Image.new('RGB', (1600, 900), (255, 255, 255))
largeimage.paste(im, (0, 0, im_size[0], im_size[1]))

draw = ImageDraw.Draw(largeimage)
draw.rectangle((10, 10, 100, 30), fill="red")
del draw

OUTPUTFILENAME = "reference_test_screenshot_tolarge3.png"
logger.info("writing {0}".format(OUTPUTFILENAME))
largeimage.save(os.path.join(tmp_folder, OUTPUTFILENAME), "PNG")


im = Image.open(CLEANBASE_FILENAME)
smallimage = im.crop((0, 0, 400, 150))

OUTPUTFILENAME = "reference_test_screenshot_tosmall.png"
logger.info("writing {0}".format(OUTPUTFILENAME))
smallimage.save(os.path.join(tmp_folder, OUTPUTFILENAME), "PNG")
