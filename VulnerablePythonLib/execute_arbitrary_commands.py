import os
import subprocess


# Simplest of simple tests. Take the argument and run it as a shell command.
def execute_arbitrary_commands(s):
    subprocess.call(s, shell=True)


# Use os.system
def execute_arbitrary_commands_2(s):
    os.system(s)


# Strip whitespace before executing
def execute_arbitrary_commands_3(s):
    new_cmd = s.strip()
    subprocess.call(new_cmd, shell=True)


# Conditionally execute
def execute_arbitrary_commands_4(s):
    if not s.startswith("sh"):
        new_cmd = "echo 'starting command'; " + s
        subprocess.call(new_cmd, shell=True)
