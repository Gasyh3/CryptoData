import os

class Config:
    # Configuration pour Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')

    # Configuration pour MongoDB
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/crypto_db')

    # Configuration pour Kafka
    KAFKA_SERVERS = os.environ.get('KAFKA_SERVERS', 'localhost:9092')
    KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'crypto-topic')

    # Autres configurations
    DEBUG = os.environ.get('DEBUG', True)
