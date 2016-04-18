#!/usr/bin/python

from urllib import request
import json

url = 'http://api.wunderground.com/api/e3f6f306bfae4a63/conditions/q/va/oakton.json'
req = request.urlopen(url).read()
decode = req.decode('utf-8')
json = json.loads(decode)

temp = str(json['current_observation']['temp_f'])
cond = str(json['current_observation']['weather'])

weather = temp + '° ' + cond

print(weather)
