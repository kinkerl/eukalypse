eukalypse
=========

koalas using koality to fight the eukalypse... and to use pixel-perfect-website-compare-tests(ppwct)!

this is a very simple library to use selenium to make screenshots of websites and compare these screenshots with reference images - what you expect the website should look like - to probe if everything looks fine.


usage
=====

for now, please take a look at the testing suit for and indepth usage. 

create a screenshot
```python
e = Eukalypse()
screenshot = e.screenshot('github_eukalypse', 'https://github.com/kinkerl/eukalypse')
```

compare a website with a reference image
```python
e = Eukalypse()
screenshot = e.compare('github_eukalypse', 'https://github.com/kinkerl/eukalypse', 'my_reference_image.png')
```

