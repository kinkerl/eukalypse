In depth Usage
========

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
