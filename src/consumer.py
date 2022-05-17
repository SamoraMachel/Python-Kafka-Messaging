from kafka import KafkaConsumer, KafkaAdminClient
from kafka.admin import NewPartitions
from kafka.structs import TopicPartition
import json

SERVER = "localhost:9092"
TOPIC = "users"

# Admin configuration
admin_client : KafkaAdminClient = KafkaAdminClient(bootstrap_servers=SERVER)
topic_partition : dict = {}
topic_partition[TOPIC] = NewPartitions(total_count=2)
admin_client.create_partitions(topic_partition)


consumer = KafkaConsumer(
    TOPIC, 
    value_deserializer=lambda x : json.loads(x),
    auto_offset_reset='earliest'
)
for msg in consumer:
    print (msg)
metrics = consumer.metrics()
print(metrics)