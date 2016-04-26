#!/usr/bin/env python

from urllib import request
import json
import os
import time
import datetime

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

apikey = open('apikey.txt').read().rstrip()

api = 'http://api.wunderground.com/api/' + apikey + '/conditions/q/va/oakton.json'
cur = 'weather.json'

if not os.path.isfile(cur):
    request.urlretrieve(api, 'weather.json')

mtime = os.path.getmtime(cur)
timediff = time.time() - mtime

if timediff > 300:
    request.urlretrieve(api, 'weather.json')

req = open(cur).read()
json = json.loads(req)

temp = str(int(json['current_observation']['temp_f']))
cond = str(json['current_observation']['weather'])

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
else:
    icon = cond

weather = icon + '  ' + temp + '°'
print(weather)
