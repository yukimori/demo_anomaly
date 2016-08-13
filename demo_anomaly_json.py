#-*- coding:utf-8 -*-

from bottle import HTTPResponse
from bottle import route, run
import json
import random

@route('/anomaly.json')
def somejson():
    
    body = json.dumps({"lof": random.random()*3.0})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    r.set_header('Access-Control-Allow-Origin', '*')
    return r

run(host='localhost', port=8188, debug=True, reloader=True)
