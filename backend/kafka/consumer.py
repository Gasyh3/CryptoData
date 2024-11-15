from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# Initialisation du consommateur Kafka
consumer = KafkaConsumer('crypto-topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='crypto-group',
                         value_serializer=lambda v: json.loads(v.decode('utf-8')))

# Initialisation de MongoDB
client = MongoClient('localhost', 27017)
db = client['crypto_db']
collection = db['crypto_data']

# Consommer et stocker les données dans MongoDB
for message in consumer:
    crypto_data = message.value
    collection.insert_many(crypto_data)
    print(f"Data inserted into MongoDB: {crypto_data}")
