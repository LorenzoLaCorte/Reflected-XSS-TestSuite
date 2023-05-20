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

    Examples: Echo with Attribute
    | page                          | parameter     | value                                      | oracle   |
    | echo-attr.php                 | name          | ' id=x tabindex=1 onfocus='alert(1)#x      | alert    |
    | echo-attr2.php                | name          | " id=x tabindex=1 onfocus="alert(1)#x      | alert    |

    Examples: Image Loaders
    | page                          | parameter     | value                                      | oracle   |
    | img-loader.php                | target        | ' id=x tabindex=1 onfocus='alert(1)#x      | alert    |
    | img-loader-protected.php      | target        | ' id=x tabindex=1 onfocus='alert(1)#x      | alert    |
    | img-loader-protected2.php     | target        | ' id=x tabindex=1 onfocus='alert(1)#x      | alert    |

    Examples: Redirect
    | page                          | parameter     | value                                      | oracle   |
    | redirect.php                  | target        | ' id=x tabindex=1 onfocus='alert(1)#x      | alert    |
    | redirect_protected.php        | target        | ' id=x tabindex=1 onfocus='alert(1)#x      | alert    |