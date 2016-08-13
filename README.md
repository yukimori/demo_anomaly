# How to use
zookeeperの起動
../kafka_2.9.2-0.8.2.2/bin/zookeeper-server-start.sh -daemon ../kafka_2.9.2-0.8.2.2/config/zookeeper.properties

kafka-serverの起動
../kafka_2.9.2-0.8.2.2/bin/kafka-server-start.sh -daemon ../kafka_2.9.2-0.8.2.2/config/server.properties

kafka-serverにデータを追加する(producer)プログラムを起動
python send_kddcup.py

/anomaly.jsonへのhttpリクエストを受け取りkafkaからデータを取得し、jubaanomalyにデータを追加し、anomaly値を取得してjsonで返却するサーバプログラムの起動
python consumer_bottle.py

jubaanomalyを起動
jubaanomaly -f anomaly_conf.json &