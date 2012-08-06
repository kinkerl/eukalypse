import unittest
from eukalypse.eukalypse import Eukalypse
import os
import Image
import ImageDraw
import shutil
import subprocess

class TestSequenceFunctions(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# temp testfolder
		cls.tmp_folder = 'tests/assets/test_tmp'
		cls.TESTURL = 'http://localhost:8400/'
		if os.path.isdir(cls.tmp_folder): # pragma: no cover
			shutil.rmtree(TestSequenceFunctions.tmp_folder)

	def setUp(self):
		if not os.path.isdir(TestSequenceFunctions.tmp_folder):
			os.mkdir(TestSequenceFunctions.tmp_folder)		
		self.e = Eukalypse()
		self.e.resolution = (1280, 768)
		self.e.browser='chrome'
		self.e.output = TestSequenceFunctions.tmp_folder
		self.e.connect()

	def tearDown(self):
		self.e.disconnect()
		#shutil.rmtree(TestSequenceFunctions.tmp_folder)

	def test_reconnect(self):
		self.assertTrue(self.e.driver!=False)
		self.e.connect()
		self.assertTrue(self.e.driver!=False)

	def test_disconnect(self):
		self.assertTrue(self.e.driver!=False)
		self.e.disconnect()
		self.assertTrue(self.e.driver==None)

	def test_screenshot(self):
		"""
		Just try to create a screenshot
		"""
		screenshot = self.e.screenshot('test_screenshot', TestSequenceFunctions.TESTURL)
		self.assertTrue(screenshot!=False)
		self.assertTrue(os.path.isfile(screenshot))

	def test_screenshot_connect(self):
		"""
		Try to create a screenshot and test the auto-connect function
		if eukalypse is not connected to the selenium server.
		"""
		self.assertTrue(self.e.driver!=False)
		self.e.disconnect()
		self.assertTrue(self.e.driver==None)
		screenshot = self.e.screenshot('test_screenshot_connect', TestSequenceFunctions.TESTURL)
		self.assertTrue(screenshot!=False)
		self.assertTrue(os.path.isfile(screenshot))

	def test_compareClean(self):
		"""
		Match against a clean screenshot and expect no error.
		"""
		response = self.e.compare('test_compareClean', 'tests/assets/reference_test_screenshot.png', TestSequenceFunctions.TESTURL)
		self._response_clean(response)

	def test_compareCleanSmallReference(self):
		response = self.e.compare('test_compareCleanSmallReference', 'tests/assets/reference_test_screenshot_tosmall.png', TestSequenceFunctions.TESTURL)
		self._response_clean(response)

	def test_compareCleanLargeReference(self):
		response = self.e.compare('test_compareCleanLargeReference', 'tests/assets/reference_test_screenshot_tolarge.png', TestSequenceFunctions.TESTURL)
		self._response_clean(response)

	def test_compareCleanLargeReferenceTainted(self):
		response = self.e.compare('test_compareCleanLargeReferenceTainted', 'tests/assets/reference_test_screenshot_tolarge2.png', TestSequenceFunctions.TESTURL)
		self._response_clean(response)


	def test_compareCleanLargeReferenceTainted2(self):
		response = self.e.compare('test_compareCleanLargeReferenceTainted2', 'tests/assets/reference_test_screenshot_tolarge3.png', TestSequenceFunctions.TESTURL)
		self._response_tainted(response)

	def test_compareTainted(self):
		"""
		Match against a tainted screenshot and get the error.
		"""
		response = self.e.compare('test_compareTainted', 'tests/assets/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL)
		self._response_tainted(response)

	def test_compareTaintedMask(self):
		"""
		Match against a tainted screenshot but use a ignore mask to 
		cut out the expected error.
		"""
		response = self.e.compare('test_compareTaintedMask', 'tests/assets/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'tests/assets/reference_test_screenshot_tainted_mask.png')
		self._response_clean(response)

	def test_compareTaintedMask2(self):
		"""
		Match with a "wrong" irgnore mask and expect a tainted error
		"""
		response = self.e.compare('test_compareTaintedMask2', 'tests/assets/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'tests/assets/reference_test_screenshot_tainted_mask2.png')
		self._response_tainted(response)


	def test_compareTaintedMask3(self):
		response = self.e.compare('test_compareTaintedMask3', 'tests/assets/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'tests/assets/reference_test_screenshot_tainted_mask_stretch.png')
		self._response_clean(response)

	def test_compareTaintedMask4(self):
		self.e.output = '.'
		response = self.e.compare('test_compareTaintedMask4', 'tests/assets/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'tests/assets/reference_test_screenshot_tainted_mask_stretch2.png')
		self._response_clean(response)

	def test_compareTaintedMask5(self):
		response = self.e.compare('test_compareTaintedMask5', 'tests/assets/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'tests/assets/reference_test_screenshot_tainted_mask_stretch3.png')
		self._response_tainted(response)

	def test_execute(self):
		"""
		Test execution of selenium statements
		"""
		statement = """
driver = self.driver
driver.get(self.base_url + "/")
driver.set_window_size(1280, 768)
driver.find_element_by_id("clickme").click()
"""
		self.e.base_url = TestSequenceFunctions.TESTURL
		self.e.execute(statement)
		response = self.e.compare('execute', 'tests/assets/reference_test_screenshot_index2.png')
		self._response_clean(response)

	def test_execute_row(self):
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

		self.e.base_url = TestSequenceFunctions.TESTURL
		self.e.execute(statement)
		response = self.e.compare('execute_row1', 'tests/assets/reference_test_screenshot_input.png')
		self._response_clean(response)

		statement = """
driver = self.driver
driver.find_element_by_css_selector('input[type="submit"]').click()
"""

		self.e.execute(statement)
		response = self.e.compare('execute_row2', 'tests/assets/reference_test_screenshot_index2.png')
		self._response_clean(response)



	def _response_clean(self, response):
		"""
		Helper function to check if a response object is clean and
		the attributes looks clean.
		"""
		self.assertTrue(response.clean)
		self.assertNotEqual(response.identifier,'')
		self.assertEqual(response.dirtiness,0)

		self.assertNotEqual(response.target_url,'')

		self.assertNotEqual(response.target_img,'')
		self.assertTrue(os.path.isfile(response.target_img))

		self.assertNotEqual(response.reference_img,'')
		self.assertTrue(os.path.isfile(response.reference_img))

		self.assertEqual(response.difference_img,'')
		self.assertTrue(not os.path.isfile(response.difference_img))

		self.assertEqual(response.difference_img_improved,'')
		self.assertTrue(not os.path.isfile(response.difference_img_improved))

	def _response_tainted(self, response):
		"""
		Helper function to check if a response object is tainted,
		the attributes look tainted and the difference images are created.
		"""
		self.assertFalse(response.clean)
		self.assertNotEqual(response.identifier,'')
		self.assertNotEqual(response.dirtiness,0)
		self.assertNotEqual(response.target_url,'')

		self.assertNotEqual(response.target_img,'')
		self.assertTrue(os.path.isfile(response.target_img))

		self.assertNotEqual(response.reference_img,'')
		self.assertTrue(os.path.isfile(response.reference_img))

		self.assertNotEqual(response.difference_img,'')
		self.assertTrue(os.path.isfile(response.difference_img))

		self.assertNotEqual(response.difference_img_improved,'')
		self.assertTrue(os.path.isfile(response.difference_img_improved))

if __name__ == '__main__':
	unittest.main()



