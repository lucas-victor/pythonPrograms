#!/usr/bin/env python3
# -*- coding; utf-8 -*-
from time import sleep
import subprocess

processo = subprocess.call(["ls", "-la"], shell=True)
#seria o mesmo que ls -la no seu terminal.

sleep(5)
#OU
input('pressione enter para sair.')