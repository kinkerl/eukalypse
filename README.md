Eukalypse
===========

Eukalypse is a library to keep the hassle of websites litmus tests away from the developer. It serves 2 main goals:

* easy way to create screenshots of websites - boring
* easy way to create screenshots of websites and compare these to an expected outcome - interesting!! 

Feature 2 can be used in and a testing environment: "is everything as i expect it to be?"
Technical speaking: Are the pixels of the current generated screenshot of a website the same as in the reference screenshot I created and verified in advance.
You can write tests using Eukalypse to verify your expections.
If you dont want to write tests or maintain a testing system yourself, you can use EukalypseNow. 
It is an experimental stand-alone tool to regulary check your sites and inform you about changes in the pixels!

And dont worry. I know content changes are pixel changes as well. Sometimes these changes needed to be tracked, sometimes they do not.
You can use the experimental feature of image masks to ignore changes in the masked areas.

You can supply features, bugs and patches at github: https//github.com/kinkerl/eukalypse  


Installation
============

You only need the eukalypse/eukalypse.py file in a place where your script will find it. Everything else is just candy. If you are lazy or care about the candy, install eukalypse using pip:

```bash
$ pip install -e git+https://github.com/kinkerl/eukalypse.git#egg=eukalypse
```

You may have to install the requirements in the requirements.txt as well. I have to streamline and clean up the installation process.

Usage
=====

Eukalypse can be used to create one or more screenshots, compare screenshots with reference images and, in addtion, can execute selenium testing code beforehand to create the state in the application you want to check.

You need a running selenium server somewhere. In this examples, it is asumed the server is running on localhost and the development test webserver is running on localhost as well. 

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

You need the webbrower chrome, a running selenium server and a testing webserver on localhost to run the tests. These are included! 

```bash
$ make start_server_selenium
$ make start_server_web
```

After the servers are started, you can create reference images for future checks, tailored to your system. These images will depend "heavily" on your operating system.

```bash
$ make generate_reference_screenshots
```

The images are now stored in tests/assets. If they look fine, run all the tests!

```bash
$ make test_feature
$ make test_unit
$ make test_pep8
```

