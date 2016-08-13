#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# 特徴名を読み込み
feature_type = []
with open("kddcup.names", "r") as f:
    f.readline()
    while True:
        line = f.readline().rstrip()
        if line == "":
            break
        # 特徴名と特徴タイプを切り分けて覚える
        feature_type.append(line.split(":"))

#print feature_type

# import sys
# sys.exit(0)

from kafka import KafkaProducer
import json
import datetime

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# データを読み込み
data = []
with open("kddcup.data.csv","r") as f:
    while True:
        line = f.readline().rstrip()
        if line == "":
            break
        features = {}
#        print line
        for schema, value in zip(feature_type, line.split(",")):
            fname,ftype = schema
            fname = fname.strip()
            ftype = ftype.strip()
            if ftype == 'continuous.':
                features[fname] = float(value)
            elif ftype == 'symbolic.':
                features[fname] = value
            else:
                print "error!!"

        data.append(features)
        producer.send('anomaly', features)
        # print features
        print "add data:", datetime.datetime.today()
        time.sleep(1)
