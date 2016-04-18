#!/bin/sh

import os
import re

cmd = "acpi"
acpi = os.popen(cmd).read()

if acpi:
    cmd = "acpi -b | grep -o '[0-9][0-9]:[0-9][0-9]'"
    time = os.popen(cmd).read().rstrip()

    cmd = "acpi -b | grep -Eo '[0-9]+%'"
    percent = os.popen(cmd).read().rstrip()

    batt = percent + ' (' + time + ')'

    print(batt)
else:
    print('####')
