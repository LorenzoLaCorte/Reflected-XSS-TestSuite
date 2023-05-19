from behave import *

from pathlib import Path
import requests
from logging import getLogger, FileHandler, DEBUG
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

NEW_LOG_EACH_RUN = True
SEC_TO_WAIT = 2

def getMyLogger(log_file):
    if os.path.isfile(log_file) and NEW_LOG_EACH_RUN: 
        os.remove(log_file)
    logger = getLogger()
    logger.addHandler(FileHandler(log_file))
    logger.setLevel(DEBUG)
    return logger

def CollectTargets(basepath):
    targets: dict[str, list[str]] = {}
    basepath = Path(basepath)
    subdirs = basepath.iterdir()

    for subdir in subdirs:
        if subdir.is_file(): continue
        targets[subdir.name] = []
        for file in subdir.iterdir():
            if file.is_file():  targets[subdir.name].append(subdir.name+'/'+file.name)

    return targets

log_file = "requests.log"
myLogger = getMyLogger(log_file)

# --------------------------- REQUEST METHODS --------------------------- #

def send_request(port, target, params, method) -> str:
    if method == "GET": 
        response = requests.get(f"http://localhost:{port}/{target}", params=params)
    elif method == "POST":
        response = requests.post(f"http://localhost:{port}/{target}", data=params)
    else:
        raise Exception(f"Error: Unrecognized Method")

    myLogger.debug(f"Sending request to: http://localhost:{port}/{target} - With params: {params}")

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")

    myLogger.debug(f"Result is: {response.text}\n")
    return response.text

def is_alert_present(page, port, parameter, value):
    driver = webdriver.Chrome() 

    url = f"http://localhost:{port}/{page}?{parameter}={value}"
    myLogger.debug(f"Selenium Alert Check in: http://localhost:{port}/{page}?{parameter}={value}")

    driver.get(url)
    isPresent = True

    try:
        WebDriverWait(driver, SEC_TO_WAIT).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        isPresent = True

    except TimeoutException:
        isPresent = False

    finally:
        driver.quit()
        return isPresent

# ------------------------------ GENERAL ------------------------------ #

@given('the server is working properly')
def step_server_working(context):
    response = send_request(port=context.port, target="index.php", params=None, method="GET")
    assert "Server is working properly" in response, "Expected server to be working properly"

@when('I send "{value}" as "{parameter}" to "{page}"')
def step_send_message(context, value, parameter, page):
    try:
        context.page = page
        context.parameter = parameter
        context.value = value
        context.response = send_request(port=context.port, target=page, params={parameter: value}, method="GET")
    except Exception as e:
        assert False, f"Failed to send request: {e}"

# ------------------------- FUNCTIONAL TESTING ------------------------- #

@then('the page should visualize "{oracle}"')
def step_page_functional_visualization(context, oracle):
    assert oracle in context.response, f"Expected '{oracle}' to be visualized"
    
# ------------------------- SECURITY TESTING ------------------------- #

@then('the page should not visualize "{oracle}"')
def step_page_security_content(context, oracle):
    if oracle not in context.response:
        assert True
    else:
        assert not is_alert_present(context.page, context.port, context.parameter, context.value)