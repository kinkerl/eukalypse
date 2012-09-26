Feature: Basic tests
    
    
    Scenario: Create a screenshot
        Given I create a screenshot with the name "test_screenshot" of the url "http://localhost:8400/"
        Then the screenshot response is not "False"
        And the file "test_screenshot.png" exists

    Scenario: Create a screenshot and test the auto-connect function
        Given I am connected to Selenium
        Then I disconnect from Selenium
        And I create a screenshot with the name "test_screenshot2" of the url "http://localhost:8400/"
        Then the screenshot response is not "False"
        And the file "test_screenshot2.png" exists
