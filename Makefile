all: test

test_unit:
	cd tests && py.test eukalypse_test.py
#nosetests --with-coverage --cover-package=eukalypse --cover-html --cover-tests tests.eukalypse_test

test_feature:
	cd tests && lettuce

test_pep8:
	pep8 eukalypse/eukalypse.py


test: test_unit, test_feature

start_server_selenium:
	cd tests/assets/ && java -Dwebdriver.chrome.driver=chromedriver -jar selenium*.jar

start_server_web:
	cd tests/assets/webroot && python ../test_server.py

generate_reference_screenshots:
	python tests/generate_test_images.py
