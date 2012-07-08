import unittest
from eukalypse import Eukalypse
import os
import Image
import ImageDraw
import shutil
import subprocess

class TestSequenceFunctions(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# temp testfolder
		cls.tmp_folder = 'test_tmp'
		cls.TESTURL = 'http://localhost:8400/'
		if os.path.isdir(cls.tmp_folder): # pragma: no cover
			shutil.rmtree(TestSequenceFunctions.tmp_folder)

	def setUp(self):
		os.mkdir(TestSequenceFunctions.tmp_folder)		
		self.e = Eukalypse()
		self.e.output = TestSequenceFunctions.tmp_folder
		self.e.connect()

	def tearDown(self):
		self.e.disconnect()
		shutil.rmtree(TestSequenceFunctions.tmp_folder)

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
		response = self.e.compare('test_compareClean', 'test/reference_test_screenshot.png', TestSequenceFunctions.TESTURL)
		self._response_clean(response)

	def test_compareTainted(self):
		"""
		Match against a tainted screenshot and get the error.
		"""
		response = self.e.compare('test_compareTainted', 'test/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL)
		self._response_tainted(response)

	def test_compareTaintedMask(self):
		"""
		Match against a tainted screenshot but use a ignore mask to 
		cut out the expected error.
		"""
		self.e.output = '.'
		response = self.e.compare('test_compareTaintedMask', 'test/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'test/reference_test_screenshot_tainted_mask.png')
		self._response_clean(response)

	def test_compareTaintedMask2(self):
		"""
		Match with a "wrong" irgnore mask and expect a tainted error
		"""
		self.e.output = '.'
		response = self.e.compare('test_compareTaintedMask2', 'test/reference_test_screenshot_tainted.png', TestSequenceFunctions.TESTURL, 'test/reference_test_screenshot_tainted_mask2.png')
		self._response_tainted(response)

	def test_execute(self):
		"""
		Test execution of selenium statements
		"""
		statement = """
driver = self.driver
driver.get(self.base_url + "/")
driver.find_element_by_id("clickme").click()
"""
		self.e.base_url = TestSequenceFunctions.TESTURL
		self.e.execute(statement)
		response = self.e.compare('execute', 'test/reference_test_execute.png')
		self._response_clean(response)

	def test_execute_row(self):
		"""
		Test multiple execution of selenium statements and compare 2 
		screenshots to verify the progress of the execution. 
		"""
		statement = """
driver = self.driver
driver.get(self.base_url + "/")
driver.find_element_by_css_selector('input[type="text"]').clear()
driver.find_element_by_css_selector('input[type="text"]').send_keys("asd")
"""

		self.e.base_url = TestSequenceFunctions.TESTURL
		self.e.execute(statement)
		response = self.e.compare('execute_row1', 'test/reference_test_execute_row1.png')
		self._response_clean(response)

		statement = """
driver = self.driver
driver.find_element_by_css_selector('input[type="submit"]').click()
"""

		self.e.base_url = TestSequenceFunctions.TESTURL
		self.e.execute(statement)
		response = self.e.compare('execute_row2', 'test/reference_test_execute.png')
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



