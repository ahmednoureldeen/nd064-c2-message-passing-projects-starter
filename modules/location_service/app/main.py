import os

from kafka import KafkaConsumer

from udaconnect.services import LocationService


TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    
    LocationService.create(message.value.decode('utf-8')) 