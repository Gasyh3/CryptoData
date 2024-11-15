import requests
from bs4 import BeautifulSoup

def scrape_crypto_data():
    url = 'https://coinmarketcap.com/historical/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Logique de scraping ici
