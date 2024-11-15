# Crypto VIZ

## Description
Crypto VIZ est une application Big Data pour la collecte, l'analyse en temps réel, et la visualisation des données des cryptomonnaies. Le projet utilise **Python**, **Kafka**, **Spark**, et **MongoDB** pour le backend.

## Fonctionnalités
1. **Scraping des données** : Collecte en continu les données des cryptomonnaies.
2. **Analyse en temps réel** : Utilisation de Spark Streaming pour traiter les données collectées.
3. **Visualisation dynamique** : Affichage en temps réel avec des graphiques de l'évolution des cryptomonnaies.

## Architecture
- **Backend** : Python, Kafka, Spark, MongoDB
- **Scraping** : BeautifulSoup, Requests
- **Visualisation** : Dash/Plotly

## Installation
1. Clonez le repository :
   ```bash
   git clone <repository-url>
   cd crypto_viz_backend

## Installation de l'environnement virtuel

1. **Créer un environnement virtuel (venv)** :
   ```bash
   python3 -m venv venv

### Activer le venv :

2. **Sur Linux/macOS***
   ```bash
   source venv/bin/activate

3. **Installer les dépendances : Une fois activé, installez les packages :**
   ```bash
   pip install -r requirements.txt