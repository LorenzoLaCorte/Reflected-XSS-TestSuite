import time
from behave import fixture, use_fixture
import os
import subprocess

# from behave4my_project.fixtures import wsgi_server
# from selenium import webdriver

# @fixture
# def selenium_browser_chrome(context):
#     # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
#     context.browser = webdriver.Chrome()
#     yield context.browser
#     # -- CLEANUP-FIXTURE PART:
#     context.browser.quit()

# def before_all(context):
#     use_fixture(wsgi_server, context, port=8000)
#     use_fixture(selenium_browser_chrome, context)
#     # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.

def before_all(context):
    context.port = 9005
    context.basepath = "Application"
    context.processes = []

    cmd = ["php", "-S", f"localhost:{context.port}"]
    cwd = os.getcwd() + (f"/{context.basepath}")
    context.processes.append(subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    time.sleep(1) # wait for the server to be running

def after_all(context):
    for process in context.processes:
        process.terminate()
        process.wait()

# def before_feature(context, feature):
#     model.init(environment='test')