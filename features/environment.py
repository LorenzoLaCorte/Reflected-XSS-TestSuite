import time
import os
import subprocess

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