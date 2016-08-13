#-*- coding:utf-8 -*-

from bottle import HTTPResponse
from bottle import route, run
import json

@route('/some.json')
def somejson():
    body = json.dumps({'message': 'hello_world'})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

run(host='localhost', port=8188, debug=True, reloader=True)
