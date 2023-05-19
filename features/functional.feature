Feature: Functional Testing
    In order to test my application,
    As a user
    I want my pages to work properly

    Scenario Outline: Testing if <page> works 
        Given the server is working properly
        When I send "<value>" as "<parameter>" to "<page>"
        Then the page should visualize "<oracle>"

    Examples: Simple Echo
    | page                          | parameter     | value     | oracle    |
    | echo.php                      | none          | none      | Welcome   |
    | echo-name.php                 | name          | lax       | lax       |
    | echo-name-protected.php       | name          | lax       | lax       |

    Examples: Echo with Attribute
    | page                          | parameter     | value     | oracle    |
    | echo-attr.php                 | name          | test      | Welcome   |
    | echo-attr2.php                | name          | test      | Welcome   |

    Examples: Image Loaders
    | page                          | parameter     | value                              | oracle                          |
    | img-loader.php                | target        | https://tinyurl.com/laxlaxlax      | https://tinyurl.com/laxlaxlax   |
    | img-loader-protected.php      | target        | https://tinyurl.com/laxlaxlax      | https://tinyurl.com/laxlaxlax   |
    | img-loader-protected2.php     | target        | https://tinyurl.com/laxlaxlax      | https://tinyurl.com/laxlaxlax   |

    Examples: Redirect
    | page                          | parameter     | value          | oracle                          |
    | redirect.php                  | target        | google.it      | google.it   |
    | redirect_protected.php        | target        | google.it      | google.it   |
