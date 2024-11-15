from pymongo import MongoClient
from ..config import Config

def get_crypto_data():
    client = MongoClient(Config.MONGO_URI)
    db = client.crypto_db
    collection = db.crypto_data
    return list(collection.find({}, {'_id': 0}))
