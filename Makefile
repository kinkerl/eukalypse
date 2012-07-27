all: test

test:
	nosetests --with-coverage --cover-package=eukalypse --cover-html --cover-tests tests.eukalypse_test
