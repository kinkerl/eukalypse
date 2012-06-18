import unittest
from eukalypse import Eukalypse
import os
import Image
import ImageDraw
import shutil

class TestSequenceFunctions(unittest.TestCase):


	@classmethod
	def setUpClass(cls):
		cls.tmp_folder = 'test_tmp'
		if os.path.isdir(cls.tmp_folder):
			shutil.rmtree(TestSequenceFunctions.tmp_folder)		

	def setUp(self):
		os.mkdir(TestSequenceFunctions.tmp_folder)		

	def tearDown(self):
		shutil.rmtree(TestSequenceFunctions.tmp_folder)		
		

	def test_screenshot(self):
		e = Eukalypse()
		e.output = TestSequenceFunctions.tmp_folder
		screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
		#screenshot generated (screenshot is not False but the filename)
		self.assertTrue(screenshot!=False)
		#file exists
		self.assertTrue(os.path.isfile(screenshot))

	def test_compareClean(self):
		e = Eukalypse()
		e.output = TestSequenceFunctions.tmp_folder
		screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
		response = e.compare('github_eukalypse_compare', 'https://github.com/kinkerl/eukalypse', screenshot)
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


	def test_compareTainted(self):
		e = Eukalypse()
		e.output = TestSequenceFunctions.tmp_folder
		screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
		#taint the screenshot to create an error
		with open(str(screenshot), 'rb') as f:
			tainted = Image.open(f)
			draw = ImageDraw.Draw(tainted)
			draw.rectangle([0, 0, 40, 40 ],  fill="green")
			tainted.save(screenshot+".png")
			del draw, tainted
			os.remove(str(screenshot))
			os.rename(str(screenshot)+".png", str(screenshot))

		response = e.compare('github_eukalypse_compare', 'https://github.com/kinkerl/eukalypse', screenshot)
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



