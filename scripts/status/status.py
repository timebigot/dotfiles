#!/usr/bin/python3

from urllib import request, error
import os
import re
import json
import datetime
import time

def weather():

    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    apikey = open('apikey.txt').read().rstrip()

    api = 'http://api.wunderground.com/api/' + apikey + '/conditions/q/va/oakton.json'
    cur = 'weather.json'

    if not os.path.isfile(cur):
        try:
            request.urlretrieve(api, 'weather.json')
        except error.URLError:
           pass

    mtime = os.path.getmtime(cur)
    timediff = time.time() - mtime

    if timediff > 300:
        try:
            request.urlretrieve(api, 'weather.json')
        except error.URLError:
           pass

    req = open(cur).read()
    obj = json.loads(req)

    temp = str(int(obj['current_observation']['temp_f']))
    cond = str(obj['current_observation']['weather'])

    now = datetime.datetime.now().hour

    if cond == 'Clear':
        if now >= 18 or now <= 7:
            icon = '🌙'
        else :
            icon = '☀'
    elif cond == 'Overcast':
        icon = '☁'
    elif cond == 'Mostly Cloudy' or cond == 'Partly Cloudy':
        icon = '⛅'
    elif cond == 'Rain':
        icon = '☂'
    elif cond == 'Fog':
        icon = '🌫'
    elif cond == 'Thunderstorm':
        icon = '⚡'
    else:
        icon = cond

    weather = icon + '  ' + temp + '°'
    return weather

def wifi():

    cmd = "iwconfig wlp2s0 | grep -Eo '\-[0-9]+ dBm'"
    wifi_dbm = os.popen(cmd).read().rstrip()

    if wifi_dbm:
        dbm = int(re.sub(r' dBm', '', wifi_dbm))
        wifi = 2 * (dbm + 100)
        # round to nearest 10
        wifi = round(wifi, -1)
        # change to str
        wifi = str(wifi)

        if wifi == '100' or wifi == '110' or wifi == '120' or wifi =='130' or wifi == '140' or wifi == '150':
            wifi = '99'

    else:
        wifi = '00'

    wifi = wifi + '%'

    return wifi

def battery():

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

        return per

def clock():
    today = datetime.datetime.today()
    cal = today.strftime('%a %m/%d · %I:%M%p').upper()
    return cal

"""
WTR = weather()
NET = wifi()
POW = battery()

print('WTR: ' + WTR + ' NET: ' + NET + ' POW: ' + POW + TIM)
"""
TIM = clock()
print(TIM)
