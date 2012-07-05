eukalypse
=========

koality to fight the eukalypse... and to use pixel-perfect-website-compare-tests(ppwct)!

this library serves 2 main goals:

* easy way to create screenshots of websites with selenium
* easy way to create screenshots of websites and compare these to an expected outcome. 

especially feature 2 can be used in and testing/unit-testing environment: "is everything as i expect it to be?"

installation
============

```bash
$ pip install -e git+https://github.com/kinkerl/eukalypse.git#egg=eukalypse
```

usage
=====

eukalypse can be used to create one or more screenshots, compare screenshots with reference images and, in addtion, can execute selenium testing code beforehand to create the state in the application you want to check.

screenshots
-------------

create a screenshot (short version)
```python
e = Eukalypse()
screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
e.disconnect()
```

create a screenshot (long version)
```python
e = Eukalypse()
e.browser = 'firefox'
e.resolution = (1280, 768)
e.platform = 'ANY'
e.host = 'http://localhost:4444'
e.connect()
screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
e.disconnect()
```

compare
-----------

compare a website with a reference image
```python
e = Eukalypse()
eukalypse_result_object = e.compare('github_eukalypse', 'my_reference_image.png', 'https://github.com/kinkerl/eukalypse')
e.disconnect()
```


execute selenium code beforehand
--------------------------------

Example:

```python
e = Eukalypse()
e.connect()

#the selenium statements we want do run before the screenshot
statement = """
driver = self.driver
driver.get(self.base_url + "/kinkerl/eukalypse")
driver.find_element_by_id("3e3065b8153e1bab152bf852e72e542726567ea7").click()
"""
e.base_url = 'https://github.com'
e.execute(statement)
e.screenshot('test')
e.disconnect()
```

You have access to "self" which is the eukalypse instance.
You can use python test code exported from the Firefox Selenium IDE for python webdriver.


For now, please take a look at the testing suit for and indepth usage. 

testing
==========

You need a running selenium server and a testing webserver on localhost to run the tests. These are included! Change in the "test" directory and start both servers.

```bash
$ java -jar selenium-server*.jar
$ python test_server.py
```

then run the tests

```bash
$ make test
```

