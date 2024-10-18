nohup zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties > logs/zookeeper.log 2>&1 &
nohup kafka-server-start /opt/homebrew/etc/kafka/server.properties > logs/kafka.log 2>&1 &
