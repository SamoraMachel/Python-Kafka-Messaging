from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'users', 
    value_deserializer=lambda x : json.loads(x)
)
for msg in consumer:
    print (msg)
metrics = consumer.metrics()
print(metrics)