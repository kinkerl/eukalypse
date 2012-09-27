from setuptools import setup

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
    zip_safe=False,
    install_requires=['selenium'],
    dependency_links=[],
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
