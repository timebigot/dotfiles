#!/usr/bin/python

import os
import re

icon = '∵'
cmd = "iwgetid -r"
wifi_id = os.popen(cmd).read().rstrip()

cmd = "iwconfig wlp2s0 | grep -Eo '\-[0-9]+ dBm'"
wifi_dbm = os.popen(cmd).read().rstrip()

dbm = int(re.sub(r' dBm', '', wifi_dbm))
wifi_per = 2 * (dbm + 100)
# round to nearest 10
wifi_per = round(wifi_per, -1)
# change to str
wifi_per = str(wifi_per)

wifi = icon + ' ' + wifi_id + ' ' + wifi_per + '%'
print(wifi)
