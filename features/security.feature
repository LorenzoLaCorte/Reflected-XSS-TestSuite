Feature: Security Testing
    In order to test my application,
    As a user
    I want my pages to be secure

    Scenario Outline: Testing if <page> is secure, also from rendering
        Given the server is working properly
        When I send "<value>" as "<parameter>" to "<page>"
        Then the page should not has the content "<oracle>"
         And the page should not render "<oracle>"

    # TODO: change value and oracle to inject
    Examples: Rendered Pages
    | page                          | parameter     | value     | oracle    |
