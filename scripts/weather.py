#!/usr/bin/python

from urllib import request
import json
import os
import time

abspath = os.path.abspath('__file__')
dirname = os.path.dirname(abspath)
os.chdir(dirname)

api = 'http://api.wunderground.com/api/e3f6f306bfae4a63/conditions/q/va/oakton.json'
cur = 'weather.json'

if not os.path.isfile(cur):
    request.urlretrieve(api, 'weather.json')

mtime = os.path.getmtime(cur)
timediff = time.time() - mtime

if timediff > 3600:
    request.urlretrieve(api, 'weather.json')

req = open(cur).read()
json = json.loads(req)

temp = str(int(json['current_observation']['temp_f']))
cond = str(json['current_observation']['weather'])

weather = temp + '° ' + cond

print(weather)
