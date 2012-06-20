eukalypse
=========

koality to fight the eukalypse... and to use pixel-perfect-website-compare-tests(ppwct)!

this library serves 2 mail goals:

* easy way to create screenshots of websites with selenium
* easy way to create screenshots of websites and compare these to an expected outcome. 

especially feature 2 can be used in and testing/unit-testing environment: "is everything as i expect it to be?"

installation
============

```bash
$ sudo pip install -e git+https://github.com/kinkerl/eukalypse.git#egg=eukalypse
```

usage
=====


create a screenshot
```python
e = Eukalypse()
screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
```

compare a website with a reference image
```python
e = Eukalypse()
eukalypse_result_object = e.compare('github_eukalypse', 'https://github.com/kinkerl/eukalypse', 'my_reference_image.png')
```

for now, please take a look at the testing suit for and indepth usage. 
