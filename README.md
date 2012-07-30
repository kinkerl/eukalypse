Eukalypse
=========

Eukalypse is a library to interact with selenium and to keep some of the hassle of screenshot testing away from the user. It serves 2 main goals:

* easy way to create screenshots of websites with selenium
* easy way to create screenshots of websites and compare these to an expected outcome. 

Especially feature 2 can be used in and testing/unit-testing environment: "is everything as i expect it to be?"

Installation
============

You can install eukalypse using pip.

```bash
$ pip install -e git+https://github.com/kinkerl/eukalypse.git#egg=eukalypse
```

Usage
=====

Eukalypse can be used to create one or more screenshots, compare screenshots with reference images and, in addtion, can execute selenium testing code beforehand to create the state in the application you want to check.

Screenshots
-------------

create a screenshot (short version)
```python
e = Eukalypse()
screenshot = e.screenshot('test', 'http://localhost:8400/')
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
screenshot = e.screenshot('test', 'http://localhost:8400/')
e.disconnect()
```

Compare 
-----------

compare a website with a reference image
```python
e = Eukalypse()
eukalypse_result_object = e.compare('test', 'my_reference_image.png', 'http://localhost:8400/')
e.disconnect()
```


Execute selenium code beforehand
--------------------------------

Example1 :

```python
e = Eukalypse()
e.connect()
#the selenium statements we want do run before the screenshot
statement = """
driver = self.driver
driver.get(self.base_url + "/")
driver.find_element_by_id("clickme").click()
"""
e.base_url = 'http://localhost:8400/'
e.execute(statement)
e.screenshot('test')
e.disconnect()
```

You have access to "self" which is the eukalypse instance.
Exported python test code from the Firefox Selenium IDE for python webdriver can be used.


You can, of course, use the webdriver object direcly:

```python
e = Eukalypse()
e.connect()
e.driver.get('http://localhost:8400/')
e.driver.find_element_by_id("clickme").click()
e.screenshot('test')
e.disconnect()
```

For now, please take a look at the testing suit for and indepth usage. 

Testing
==========

You need the webbrower chrome, a running selenium server and a testing webserver on localhost to run the tests. These are included! Change in the "tests/assets/" directory and start the selenium and the testing webserver.

```bash
$ make start_server_selenium
$ make start_server_web
```

After the servers are started, you can run the tests.

```bash
$ make test_feature
$ make test_unit
$ make test_pep8
```

The reference images are created on Ubuntu 12.04. If you are NOT running Ubuntu 12.04, most of these tests might fail due to different font renderings on other operating systems.
