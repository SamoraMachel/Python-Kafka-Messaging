from kafka import KafkaProducer
import json

TOPIC = 'users'



producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    compression_type='gzip'
)
user_input : str = ""
partition = 0

while user_input != "q":
    user_input : str = input("Enter a message : ")
    producer.send(TOPIC, {"input": user_input})
    if user_input == 'q':
        break
    else:
        producer.flush()