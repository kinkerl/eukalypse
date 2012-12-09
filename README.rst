eukalypse
=============

.. image:: https://secure.travis-ci.org/kinkerl/eukalypse.png
    :alt: Travis CI Build Status

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


Python support
--------------

Right now, eukalypse does not support python 3.2 or jython. Its close! Mostly due to problems in third party libraries. It does however support the following:

* python 2.6
* python 2.7
* pypy

If anyone knows how to make it run on python 3.2 or jython: Tell me!


Usage
=====

Eukalypse can be used to create one or more screenshots, compare screenshots with reference images and, in addtion, can execute selenium testing code beforehand to create the state in the application you want to check.

You need a running selenium server somewhere. In this examples, it is asumed the server is running on localhost and the development test webserver is running on localhost as well. 

Screenshots
-------------

create a screenshot (short version)

.. code-block:: python

   e = Eukalypse()
   screenshot = e.screenshot('test', 'http://localhost:8400/')
   e.disconnect()

Compare 
-----------

compare a website with a reference image

.. code-block:: python

   e = Eukalypse()
   eukalypse_result_object = e.compare('test', 'my_reference_image.png', 'http://localhost:8400/')
   e.disconnect()
   if eukalypse_result_object.clean:
       print "the same!"
   else:
       print "different!"

For now, please take a look at the files in the docs folder, the examples or the testing suit for and indepth usage. 

Resources
---------

* `Documentation <http://eukalypse.readthedocs.org/>`_

