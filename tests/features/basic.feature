Feature: Basic tests
    
    
    Scenario: test screenshot
        Given the test environment is created
        And the connection is established
        When I create a screenshot with the name "test_screenshot" of the url "http://localhost:8400/"
        Then the screenshot response is not "False"
        And the file "test_screenshot.jpg" exists
        Then the connection is closed
        And the environment is cleaned
