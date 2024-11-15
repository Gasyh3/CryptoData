from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StringType, DoubleType
from pymongo import MongoClient

# Initialiser Spark
spark = SparkSession.builder \
    .appName("CryptoDataProcessor") \
    .master("local[*]") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/crypto_db.crypto_data") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/crypto_db.crypto_processed") \
    .getOrCreate()

# Schéma des données de cryptomonnaie
schema = StructType() \
    .add("name", StringType()) \
    .add("symbol", StringType()) \
    .add("price", StringType())

# Lire les données de Kafka
crypto_data = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "crypto-topic") \
    .load() \
    .selectExpr("CAST(value AS STRING)")

# Convertir les données Kafka en DataFrame Spark
crypto_df = crypto_data.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Transformation des données (par exemple : convertir les prix en Double)
crypto_df = crypto_df.withColumn("price", col("price").cast(DoubleType()))

# Définir la sortie de MongoDB
def write_to_mongodb(batch_df, batch_id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client.crypto_db
    collection = db.crypto_processed
    records = batch_df.collect()
    for record in records:
        collection.insert_one(record.asDict())

# Ecriture des résultats dans MongoDB en utilisant foreachBatch
query = crypto_df.writeStream \
    .outputMode("append") \
    .foreachBatch(write_to_mongodb) \
    .start()

# Attendre que le streaming se termine
query.awaitTermination()
