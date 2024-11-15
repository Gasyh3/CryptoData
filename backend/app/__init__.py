from flask import Flask
from .config import Config
from .routes.crypto_routes import crypto_bp

def create_app():
    # Initialisation de l'application Flask
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enregistrement des blueprints pour les routes
    app.register_blueprint(crypto_bp, url_prefix='/api/crypto')

    # Autres configurations ou extensions (e.g., MongoDB, Kafka, etc.)
    # ex : db.init_app(app)

    return app
