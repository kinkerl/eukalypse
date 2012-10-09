Usage in Unittests
==============

lets say you want to mix eukalypse unittests with your normal tests but you dont want to run the eukalypse tests everytime or in the same environment as your normal unit tests.
use decorators!


.. code-block:: python
  :linenos:

   import unittest
   from eukalypse import MSG_NEED_EUKALYPSE
   class MyFuncTestCase(unittest.TestCase):
       @unittest.skipUnless(settings.TEST_USE_EUKALYPSE, MSG_NEED_EUKALYPSE)
       def testBasic(self):
           assert 1 == 1


settings.TEST_USE_EUKALPSE is a boolean value in the settings if eukalypse unit tests should be run in this environment. 
