Feature: Functional Testing
    In order to test my application,
    As a user
    I want my pages to work properly

    Scenario Outline: Testing if <page> works 
        Given the server is working properly
        When I send "<value>" as "<parameter>" to "<page>"
        Then the page should visualize "<oracle>"

    Examples: Echo Pages
    | page                          | parameter     | value     | oracle    |
    | echo.php                      | none          | none      | Welcome   |
    | echo-name.php                 | name          | ciao      | ciao      |
    | echo-name-protected.php       | name          | ciao      | ciao      |

