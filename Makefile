all: test

test_unit:
	nosetests --with-coverage --cover-package=eukalypse --cover-html --cover-tests tests.eukalypse_test

test_feature:
	cd tests && lettuce

test_pep8:
	pep8 eukalypse/eukalypse.py


test: test_unit, test_feature

start_server_selenium:
	cd tests/assets/ && java -Dwebdriver.chrome.driver=chromedriver -jar selenium*.jar

start_server_web:
	cd tests/assets/ && python test_server.py
