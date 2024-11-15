from kafka import KafkaProducer
import requests
from bs4 import BeautifulSoup
import json

# Initialisation du producteur Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Fonction pour scraper les données
def scrape_data():
    url = 'https://coinmarketcap.com/historical/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    crypto_data = []

    tr = soup.find_all('tr', attrs={'class': 'cmc-table-row'})
    count = 0
    for row in tr:
        if count == 10:
            break
        count += 1

        name_column = row.find('a', attrs={'class': 'cmc-table__column-name--name'})
        crypto_name = name_column.text.strip()

        crypto_symbol = row.find('td', attrs={'class': 'cmc-table__cell--symbol'}).text.strip()
        crypto_price = row.find('td', attrs={'class': 'cmc-table__cell--price'}).text.strip()

        crypto_data.append({
            'name': crypto_name,
            'symbol': crypto_symbol,
            'price': crypto_price
        })

    return crypto_data

# Envoyer les données au topic Kafka
if __name__ == "__main__":
    crypto_data = scrape_data()
    producer.send('crypto-topic', crypto_data)
    producer.flush()
    print("Data sent to Kafka successfully.")
