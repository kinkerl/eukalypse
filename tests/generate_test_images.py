"""
#4 basic images
reference_test_screenshot.png
reference_test_screenshot_index2.png
reference_test_screenshot_input.png
reference_test_screenshot_tainted.png


#mods
reference_test_screenshot_tolarge.png
reference_test_screenshot_tolarge2.png
reference_test_screenshot_tolarge3.png
reference_test_screenshot_tosmall.png
"""
import sys
import os
import inspect
sys.path.append(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())),'../eukalypse'))
from eukalypse import Eukalypse
import Image, ImageDraw

tmp_folder = 'tests/assets'
e = Eukalypse()
e.resolution = (1280, 768)
e.browser='chrome'
e.output = tmp_folder
e.connect()
screenshot = e.screenshot('reference_test_screenshot', 'http://localhost:8400/index.html')
screenshot = e.screenshot('reference_test_screenshot_index2', 'http://localhost:8400/index2.html')

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

im = Image.open(os.path.join(tmp_folder,"reference_test_screenshot.png"))
draw = ImageDraw.Draw(im)
draw.rectangle((10, 10,100,30), fill="red")
del draw 

# write to stdout
im.save(os.path.join(tmp_folder ,"reference_test_screenshot_tainted.png"), "PNG")


# 3 large
im = Image.open(os.path.join(tmp_folder,"reference_test_screenshot.png"))
im_size = im.size
largeimage = Image.new('RGB', (1600,900), (255,255,255))
largeimage.paste(im, (0, 0, im_size[0], im_size[1]))

largeimage.save(os.path.join(tmp_folder ,"reference_test_screenshot_tolarge.png"), "PNG")

#
im = Image.open(os.path.join(tmp_folder,"reference_test_screenshot.png"))
im_size = im.size
largeimage = Image.new('RGB', (1600,900), (255,255,255))
largeimage.paste(im, (0, 0, im_size[0], im_size[1]))

draw = ImageDraw.Draw(largeimage)
draw.rectangle((1550, 850,1600,900), fill="red")
del draw 

largeimage.save(os.path.join(tmp_folder ,"reference_test_screenshot_tolarge2.png"), "PNG")



#-----
im = Image.open(os.path.join(tmp_folder,"reference_test_screenshot.png"))
im_size = im.size
largeimage = Image.new('RGB', (1600,900), (255,255,255))
largeimage.paste(im, (0, 0, im_size[0], im_size[1]))

draw = ImageDraw.Draw(largeimage)
draw.rectangle((10, 10,100,30), fill="red")
del draw 

largeimage.save(os.path.join(tmp_folder ,"reference_test_screenshot_tolarge3.png"), "PNG")


# 1 small


im = Image.open(os.path.join(tmp_folder,"reference_test_screenshot.png"))
smallimage =  im.crop((0,0,400,150))

smallimage.save(os.path.join(tmp_folder ,"reference_test_screenshot_tosmall.png"), "PNG")

