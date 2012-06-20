from setuptools import setup
import finddata


setup(
    name="eukalypse",
    author="Dennis Schwertel",
    author_email="s@digitalkultur.net",
    version='0.1',
    packages=['eukalypse'],
    package_data=finddata.find_package_data(),
    url='https://github.com/kinkerl/eukalypse',
    include_package_data=True,
    license='MIT',
    description='koality to fight the eukalypse... and to use pixel-perfect-website-compare-tests(ppwct)!',
    long_description=open('README.md').read(),
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
