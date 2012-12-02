"""
Eukalypse is a library to create screenshots and compare them

"""

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name="eukalypse",
    author="Dennis Schwertel",
    author_email="s@digitalkultur.net",
    version='0.1.1',
    url='https://github.com/kinkerl/eukalypse',
    license='MIT',
    zip_safe=False,
    packages=['eukalypse'],
    package_data={'eukalypse': ['screenshot.js']},
    description='Compare websites to images of websites and spots the difference.',
    long_description=__doc__,
    install_requires=['selenium', 'pillow'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]
)
