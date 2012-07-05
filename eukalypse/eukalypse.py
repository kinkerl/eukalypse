#!/usr/bin/env python
from selenium import webdriver
import time
import Image
import ImageChops
import os


class EukalypseCompareResponse:
    """
    A Response is the result of a comparison. It holds all the information needed to display what happend and what the outcome is.
    """

    def __init__(self):
        self.identifier = ''
        self.clean = True
        self.dirtiness = 0
        self.target_img = ''
        self.target_url = ''
        self.reference_img = ''
        self.difference_img = ''
        self.difference_img_improved = ''
        self.base_url = ''


class Eukalypse:
    def __init__(self):
        self.wait = 0
        self.browser = 'firefox'
        self.resolution = (1280, 768)
        self.platform = 'ANY'
        self.host = 'http://localhost:4444'
        self.output = '.'
        self.ignoremask = False
        self.improve_factor = 100
        self.driver = None

    def connect(self):
        """
        Creates a connection to the Selenium Server which exists until it is disconnected.
        You can execute multiple commands, screenshots or compare within one connection.
        Chained commands start where the leading command stops.
        """
        if self.driver:
            self.driver.disconnect()
        self.driver = webdriver.Remote("%s/wd/hub" % self.host,
                                desired_capabilities={
                                    "browserName": self.browser,
                                    "platform": self.platform,
                                })

    def disconnect(self):
        """
        If a connection exists, try to disconnect from it.
        """
        try:
            if self.driver:
                self.driver.close()
        except:  # pragma: no cover
            pass

    def execute(self, statement):
        """
        driver = self.driver
        driver.get(self.base_url + "/kinkerl/eukalypse")
        driver.find_element_by_link_text("Downloads 0").click()
        """
        exec(statement, {"__builtins__":None},{"self":self})

    def screenshot(self, identifier, target_url=None):
        """
        Generate a screenshot of the target_url and save it in the output directory(self.output).
        The filename will be the identifier + ".png".
        If no target_url is given, try  to make a screenshot of the current connection state.
        This is usefull if you start with selenium commands run with execute and want to test or shot the resulting state of the commands.
        """
        destination = False
        if not self.driver:  # pragma: no cover
            self.connect()
        try:
            self.driver.set_window_size(self.resolution[0], self.resolution[1])
            if target_url:
                self.driver.get(target_url)
            time.sleep(self.wait)
            destination = os.path.join(self.output, "%s.png" % identifier)
            self.driver.get_screenshot_as_file(destination)
        except Exception:  # pragma: no cover
            raise

        return destination

    def compare(self, identifier, reference_image, target_url=None):
        """
        Generate a screenshot of the target_url and compare it with the reference image.
        The filename will be the identifier + ".png".
        If no target_url is given, try to compare the current connection state.
        If an error occured, the Response object will not be "clean" and a difference and an improved difference image are created. 
        The paths to these images are part of the response object.
        """

        response = EukalypseCompareResponse()
        response.identifier = identifier
        response.target_url = target_url
        response.reference_img = reference_image

        target_image = self.screenshot(identifier, target_url)
        response.target_img = target_image

        im1 = Image.open(target_image)
        im2 = Image.open(reference_image)

        diff = ImageChops.difference(im2, im1)

        #if an ignoremask exist, multiply it with the difference. this makes
        #everything black in the diff which is black in the ignoremask
        if self.ignoremask:
            imignore = Image.open(self.ignoremask)
            diff = ImageChops.multiply(imignore, diff)
        colors = diff.getcolors(diff.size[0] * diff.size[1])

        #get differences. only notblack pixels show a difference
        black = 0
        notblack = 0
        for color in colors:
            if color[1] == (0, 0, 0, 0) or color[1] == (0, 0, 0):
                black += color[0]
            else:
                notblack += color[0]
        if notblack == 0:
            response.clean = True
        else:
            response.clean = False
            response.dirtiness = 100. * notblack / (notblack + black)

            diff_filename = os.path.join(
                self.output,
                "%s-difference.jpg" % identifier
            )
            diff.save(diff_filename, "JPEG", quality=100)
            response.difference_img = diff_filename

            im = Image.open(diff_filename)
            im = im.convert('RGB')
            r, g, b = im.split()
            r = r.point(lambda i: i * self.improve_factor)
            g = g.point(lambda i: i * self.improve_factor)
            b = b.point(lambda i: i * self.improve_factor)
            out = Image.merge('RGB', (r, g, b))
            diff_imp_filename = os.path.join(
                self.output,
                "%s-difference-improved.jpg" % identifier
            )
            out.save(diff_imp_filename, "JPEG", quality=100)

            response.difference_img_improved = diff_imp_filename
        return response

if __name__ == '__main__':
    pass
