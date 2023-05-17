# Third Assignment - Reflected XSS
In this assignment, you will build an additional module for your test suite to test for Reflected XSS.
Notice that not all pages in the target are vulnerable, and some pages might require specific payloads to be exploited.

Here you can find the instructions to build the test suite for your assignment.

## Create your testing scenarios
During our last lesson, I showcased behave, a Python tool that parses files written in Gherkin syntax, and helps you in organizing and running your tests, which you can gather in features and steps.

For this assignment, you will write (at least) two scenarios for each page in the target:
- A baseline scenario to test that the page is working correctly
- A malicious scenario to test if the page is vulnerable to Reflected XSS 
- (if you can apply multiple attack payloads, you can choose to implement only one in this scenario)

You can store scenarios in a folder called "/features" in the same directory as the target environment. For reference, here is the example nosqli.feature file that I showed you during the lesson:

Feature: Absence of SQLi in my application

  Scenario: the application is resilient to single quotes
    Given the application login page
     When an attacker tries to input the ' character
     Then the application will return an error

  Scenario: the application is resilient to double quotes
    Given the application login page
     When an attacker tries to input the " character
     Then the application will return an error
How you decide to group scenarios in features is completely up to you.

## Convert scenarios into test steps
After you wrote these scenarios, run the "behave" command in your directory.

If you haven't created a "features/steps" folder yet, this should give you an error saying "ConfigError: No steps directory". If that's the case, just create a "features/steps" folder.

Running the tool again should give you a warning message, saying that your tests failed, followed by "You can implement step definitions for undefined steps with these snippets:" (followed by the parsed snippets for your test steps).

You can copy all these steps in any ".py" file in your "features/steps" folder (just make sure that all the files start with "from behave import *").

For more details on this process, please refer to the documentation. If you have any problems on this part of the assignment (or any other part), write your problem on the forum so we can solve it quickly.

After you created these support functions, you can now start implementing the actual logic for your test steps.

## Writing your test steps
Now that you have the scaffolding for your test steps, you should start implementing them.

The logic is pretty simple, since you can insert the payload and check the response in the same page. 

- As for Functional Tests, you should simply check that the page behaves correctly (any check will do, e.g., check if the page actually displays your name in "echo-name.php").

- As for Security Tests, we need an additional confirmation step. Checking if the payload is inserted in the page is not enough here, since the exploit could not trigger due to the context it is printed into (e.g., if we try to insert a <script>alert(1)</script> payload inside an HTML attribute, instead of an HTML tag).

## Selenium
To confirm that the payload actually works, we can check that the HTML is actually parsed and rendered on the page, and we can automate this check via the Selenium Web Driver (you should already be familiar with this tool from the Functional Testing part of this course).

However, Selenium is quite slow in performing this check, so we want to use it sparingly to confirm a vulnerability. For example, there is no need to perform a check with Selenium if the page does not display any of my content (see the echo.php page).

## Payload
You should find the right payload for each page, but here are some suggestions for choosing the payload:

- Use a payload that triggers an alert() function (you can choose the content, be careful that some payloads might fail due to quotes or double quotes)
- Choose the simplest payload for any page (don't use complicated polyglot payloads, they might work on the short term, but they will fail in really creative ways, and it might take a long time to debug)
- Whenever possible, choose the payload that does not require user interaction (for a list of XSS payloads, you can check the PortSwigger XSS CheatSheet) 
Summary

## Summary
Here's a quick summary of the process you should follow for this assignment:

- Create your scenarios, at least:
    - one "benign", 
    - one "malicious", with the actual exploit (if any)

- Convert scenarios into test steps with behave
- You can use behave to create the scaffolding, no need to write all of them by hand

- Implement your test steps; in each step you should:
    - Check if the page is working correctly
    - Check if the page can be attacked
    - Check that the response contains your payload (without rendering the page)

- ONLY if it the page contains your payload, run Selenium to confirm the vulnerability 