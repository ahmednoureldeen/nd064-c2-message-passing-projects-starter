import json
import os

from kafka import KafkaProducer


TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)



def save_location(location_data):
    # Kafka producer has already been set up in Flask context
    
    # Turn location_data into a binary string for Kafka
    kafka_data = json.dumps(location_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = producer
    kafka_producer.send(TOPIC_NAME, kafka_data)