Feature: Security Testing
    In order to test my application,
    As a user
    I want my pages to be secure

    Scenario Outline: Testing if <page> is secure, also from rendering
        Given the server is working properly
        When I send "<value>" as "<parameter>" to "<page>"
        Then the page should not visualize "<oracle>"

    Examples: Simple Echo
    | page                          | parameter     | value                          | oracle   |
    | echo.php                      | name          | <script>alert(42)</script>     | alert    |
    | echo-name.php                 | name          | <script>alert(42)</script>     | alert    |
    | echo-name-protected.php       | name          | <script>alert(42)</script>     | alert    |