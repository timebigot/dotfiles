#!/usr/bin/python

import os
import re
from termcolor import colored

cmd = "acpi"
acpi = os.popen(cmd).read()

icon = ''

if acpi:
    cmd = "acpi -b | grep -Eo '[0-9]+%'"
    per = os.popen(cmd).read().rstrip()

    cmd = "acpi -b | grep -o '[0-9][0-9]:[0-9][0-9]'"
    time = os.popen(cmd).read().rstrip()

    cmd = "acpi -b | grep -o 'Charging'"
    state = os.popen(cmd).read().rstrip()

    per_int = int(per.replace('%', ''))

    if per == '100%':
        per = colored(per, 'green')
        time = '00:00'
        icon ='❇'
    elif state == 'Charging':
        icon = '⚡️'
    elif per_int <= 10:
        icon = '♥'
    elif not state:
        icon = '♡'
else:
    per = '##%'
    time = '##:##'
    icon = '☹'

battery = icon + ' ' + per
print(battery)
