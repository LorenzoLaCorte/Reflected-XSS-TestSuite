# Third Assignment - Reflected XSS
This is a simple behave test suite for Reflected XSS.

# Run the Testsuite
To run the testsuite, simply use the command:
```
behave
```

Or, if you want logs to be reported on ```requests.log```, use:
```
behave --no-logcapture
```

## Tests
This testsuite contains:

- Two scenarios:
    - functional testing: a "benign" scenario that tests if page works correctly, 
    - security testing: a "malicious" scenario, with a set of potential exploits. 

- Scenarios are converted into test steps through **behave scaffolding**
``` *.feature -> environment.py (before all and after all methods) -> steps.py ```

- For each page, the test suite:
  - Checks if the page is working correctly,
  - Checks if the page can be attacked,
  - Checks that the response contains the injection payload (without rendering the page).
  - Only if it the page contains the payload, run Selenium to render the page and eventually confirm the vulnerability.

## Attack Payloads
Injection payloads are the combination of:
- quotes or double quotes to escape HTML base tag,
- an alert() function (the easiest way to check for an XSS),
- combinations of listeners and other tags that enable the payload to work without user interaction.