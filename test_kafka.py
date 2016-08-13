# -*- coding: utf-8 -*-

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for _ in range(100):
    producer.send('topic', 'message1')

producer.flush()

from kafka import KafkaConsumer
# auto_offset_resetをearliestにしないとconsumer起動前のメッセージが読み込めない
# defaultはlatest
# ref:http://kafka-python.readthedocs.io/en/master/apidoc/kafka.consumer.html
consumer = KafkaConsumer(bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
consumer.subscribe(['topic'])
for msg in consumer:
    print msg

# # 送信用のクライアントを作成
# producer = kafka.SimpleProducer(kafka_client)

# # 'my-topic' というトピックにいくつかメッセージを送ってみる
# producer.send_messages('my-topic', 'message1')
# producer.send_messages('my-topic', 'message2')
# producer.send_messages('my-topic', 'message3')


# # この段階で Kafka のサーバには my-topic というトピックができていて、
# # message[1|2|3] が保存されている

# # my-topic に対してデータを取りに行く
# consumer = kafka.KafkaConsumer(
#     'my-topic2', 
#     bootstrap_servers=['localhost:9092'])

# # メッセージの subscribe (for文をいきなり回せば勝手にリクエストしてくれる)
# for message in consumer:
#     # print("topic: %s message=%s" % (message.topic, message.value))
#     print message.topic
