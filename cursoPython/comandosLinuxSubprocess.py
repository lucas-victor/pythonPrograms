import subprocess
from time import sleep

processo = subprocess.call("ls -la", shell=True)

sleep(5)
