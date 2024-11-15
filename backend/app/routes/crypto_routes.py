from flask import jsonify, request
from . import crypto_bp
from ..services.data_loader import get_crypto_data

@crypto_bp.route('/data', methods=['GET'])
def get_crypto_data_route():
    data = get_crypto_data()
    return jsonify(data), 200
