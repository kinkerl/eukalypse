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
    version='0.1',
    packages=['eukalypse'],
    url='https://github.com/kinkerl/eukalypse',
    license='MIT',
    description='Compare websites to images of websites and spots the difference.',
    long_description='Compare websites to images of websites and spots the difference.',
    install_requires=['selenium', 'PIL', 'configobj'],
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
