from pymongo import MongoClient

def init_db():
    # Connexion à MongoDB
    client = MongoClient('localhost', 27017)
    
    # Création de la base de données et des collections
    db = client['crypto_db']
    crypto_collection = db['crypto_data']
    
    print("MongoDB initialized successfully")
    return crypto_collection

if __name__ == "__main__":
    init_db()
