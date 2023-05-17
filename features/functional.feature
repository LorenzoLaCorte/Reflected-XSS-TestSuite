Feature: Functional Testing
    In order to test my application,
    As a user
    I want my pages to work properly

    Scenario: Testing if echo.php works 
        Given the server is working properly
        When I send "nothing" as "name" to "echo.php"
        Then the page should visualize "Welcome"