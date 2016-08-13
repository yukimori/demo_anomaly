#-*- coding:utf-8 -*-

from bottle import HTTPResponse
from bottle import route, run
import json
import random

@route('/anomaly.json')
def somejson():
    for message in consumer:
        #    print message.value
        datum = json.loads(message.value)
        print datum
        result = client.add(Datum(datum))
        print result
        break

    if result.score > 5.0:
        result.socre = 5.0
    # body = json.dumps({"lof": random.random()*3.0})
    body = json.dumps({"lof": result.score})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    r.set_header('Access-Control-Allow-Origin', '*')
    return r

from kafka import KafkaConsumer
#consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['anomaly'])

import jubatus
from jubatus.common import Datum
client = jubatus.Anomaly('127.0.0.1', 9199, 'anomaly')

import json

run(host='localhost', port=8188, debug=True, reloader=True)
