from flask import Blueprint

# Création du blueprint pour les routes liées aux cryptomonnaies
crypto_bp = Blueprint('crypto', __name__)

# Import des routes spécifiques
from . import crypto_routes
