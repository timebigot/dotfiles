#!/usr/bin/python

import os

cmd = "amixer sget Master | grep -Eo '[0-9]+%'"
vol_per = os.popen(cmd).read().rstrip()

icon = '🎵'

if vol_per == '0%':
    icon = '❌'

vol = icon + ' ' + vol_per
print(vol)
