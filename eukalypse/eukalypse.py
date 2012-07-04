#!/usr/bin/env python
from selenium import webdriver
import time
import Image
import ImageChops
import os


class EukalypseCompareResponse:
    def __init__(self):
        self.identifier = ''
        self.clean = True
        self.dirtiness = 0
        self.target_img = ''
        self.target_url = ''
        self.reference_img = ''
        self.difference_img = ''
        self.difference_img_improved = ''


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

    def connect(self):
        return webdriver.Remote("%s/wd/hub" % self.host,
                                desired_capabilities={
                                    "browserName": self.browser,
                                    "platform": self.platform,
                                })

    def screenshot(self, identifier, target_url):
        """
        generate a screenshot from a target url
        """
        destination = False
        browser = self.connect()
        try:
            browser.set_window_size(self.resolution[0], self.resolution[1])
            browser.get(target_url)
            time.sleep(self.wait)
            destination = os.path.join(self.output, "%s.png" % identifier)
            browser.get_screenshot_as_file(destination)
        except Exception:  # pragma: no cover
            raise
        finally:
            browser.close()
        return destination

    def compare(self, identifier, target_url, reference_image):
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
