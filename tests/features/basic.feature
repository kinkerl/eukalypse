Feature: Basic tests
    
    
    Scenario: test screenshot
        Given I create a screenshot with the name "test_screenshot" of the url "http://localhost:8400/"
        Then the screenshot response is not "False"
        And the file "test_screenshot.png" exists

