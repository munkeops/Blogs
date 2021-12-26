---
layout: post
title: "A Quick Introduction to Kafka with docker and python"
author: munkeops
categories: [kafka, python, docker]
image: "https://i.ytimg.com/vi/JYNEwSfWaNc/maxresdefault.jpg"
featured: true
hidden: false
---



Kafka is a very popular fault tolerant, distributed and scalable Stream Service provided by Apache as an Open Source Product. Paid alternatives (confluence) are also available for more advance features and handy tools that can be used to administer setup and monitor Kafka streams. 



## So what is Kafka?

To put in simple terms Kafka is an:

* Popular option for msg and data communication between distributed architectures (like microservices)
* It follows and facilitates the publish-subscribe method of communication.
* Streaming data means it maintains the order of data.
* Built in Java and acts as a wrapper on regular socket stream with a whole bunch of stability and expansive features.

So without much delay lets understand the structure and concepts involved when using Kafka. 

## Key Points:

### Topics

1. Kafka topics is used to identify a unique stream for reading and writing
2. It generally is used to keep similar data together
3. Similar data must be streamed under a single Kafka topic
4. Named by the user
5. Each Kafka Topic can be split into partitions

### Partitions

1. Physical splits/partitions of a topic
2. Within each partition data is ordered, that is the way data comes in is the same way data goes out
3. Can be n number of partitions for each topic
4. Data and its order in the partitions is maintained by an offset value
5. Data once written to a partition cannot be changed

### Brokers
1. Physical and independent process/devices running Kafka are like brokers
2. A Kafka cluster may contain multiple brokers
3. Partitions may be spread across brokers
4. Generally brokers are used to maintain copies of messages in each partition, thereby horizontally scaling and having a back up mechanism

### Replication
1. Each kafka topic in a kafka cluster can define a replication factor
2. Replication factors determine how many times a partition will be replicated and distributed over the brokers in a kafka cluster.
3. Kafka has a mechanism to always make sure replicas are upto date with the original partition, it also assigns leader and replica tags to multiple copies thereby maintaining order and understanding between replicas
4. As long as the leader exists no replica will serve, only the leader will the replicas will only be in sync also called ISR(in-sync-replica)
5. If the broker with the leader fails a replica will take over leadership and if the original leader comes back the replica will forfeit its leadership role

## Kafka Producers
1. A producer will write data to the topic/partition
2. Producers will be configured to know which broker and which partition and which topics to write to.
3. The producer uses message keys and acknowledgement to make sure data is added to the Kafka stream
4. Message keys help maintain order of data being sent.
5. They also help send data to any random partition or a partition of choice
6. Once a key is applied to data the message will always go to the same partition where all the keys with that value went. Generally, if no key is applied it 7. assigns keys in a round robin manner, thereby inserting to different partitions in a round robin manner therefore acting like a load balancer.
8. Key value NULL specifics, no keys assigned hence round robin
9. After writing to a partition in a broker it waits for an act, if no ack received it assumes the broker is dead and hence sends it into a replica with leader status
But ack can be configured to behave differently
10. Acknowledgement
* Ack = 0 doesn't wait for ack<br>
* Ack = 1 waits for leader ack <br>
* Ack = all wait for leader to receive and replicate to all replicas (safest and slowest)

## Kafka Consumer and Consumer groups
1. Consumer reads messages from a topic/partition.
2. Once a message is read, it still remains in the topic/partition automatic deletes need to be configured from the default time.
3. Groups are defined for synchronised reads from a partition, that is two of them could read from the same partition, so in case one fails or takes too long to respond the other takes over. 
4. A message is considered "read" for good (like to even its consumer group) by a consumer if it's committed.
5. You can define when to commit (after a set of messages read or after every message)
6. You can also define how long before the consumer stops checking for message (in case producer has not produced anything)
7. An offset marker is used to point to the current location read, when and suppose the consumer stops and then restarts it can continue from where it left off or start fresh.



### Installing and running Kafka with Docker

Instead of installing Kafka on your bare machine you can simply run it as a docker container, thereby maintaining a separate virtualized space for it and not having to deal with messy configuration and setups. (For more on how and why dockers are awesome read my other blog on docker). 

Given that docker is installed and available on your device make sure docker-component is also installed. Running Kafka on any machine also requires apache Zookeeper running in parallel to maintain and orchestrate the distributed nature of Kafka. Hence we will be running Zookeeper as separate image in this way we can start up multiple Kafka containers for distributed loads. Hence the need for docker-compose so that we can run multiple containers with a single file. The docker-compose file will look as shown below:

```yaml
version: '3'
services:
  zookeeper:
    image: wurstmeister/zookeeper
    ports:
      - "2181:2181"
  kafka:
    image: wurstmeister/kafka
    ports:
      - 9092:9092
    environment:
      KAFKA_ADVERTISED_HOST_NAME: 192.168.29.10
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_CREATE_TOPICS: "test-topic:5:2"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

```
In the above script we are using docker images created by wurstmeister as they are easy to configure and run. With the above script we are running Zookeeper and exposing it on port 2181 and then running Kafka and exposing it to port 9092. We are also setting some environment variable to configure Kafka.
* KAFKA_ADVERTISED_HOST_NAME suggests the IP at which kafka will be identified. 
* KAFKA_ZOOKEEPER_CONNECT points to the port zookeper can be found at.
* KAFKA_CREATE_TOPICs will create a topic test-topic with 5 paritions and 2 replicas.

Now run the docker-compose file as show below and if no errors show up, Kafka has successfully been installed and will be running on port 9092.

```bash
docker-compose up
```
### Setup Python to use with kafka

```bash
pip install kafka-python
```

### Kafka producer in python
```python
from time import sleep
from json import dumps
from kafka import KafkaProducer
 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
 
for e in range(1000):
    data = {'number' : e}
    producer.send('items-list', value=data)
    print(e)
    sleep(5)
```


### Kafka Consumer in python

```python
from kafka import KafkaConsumer
from json import loads
from time import sleep
 
 
consumer = KafkaConsumer(
    'items-list',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='items-group',
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
 
 
for message in consumer:
   print(message.value)

```

### Conclusion

I hope this post helped you in understanding Kafka concepts and gave you a place to begin with developing you python application with Kafka.