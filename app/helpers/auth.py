from functools import wraps
from flask import request, jsonify

TOKEN_FIXO = "powerofdata123"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Unauthorized"}), 401

        try:
            scheme, token = auth_header.split(" ")
        except ValueError:
            return jsonify({"error": "Unauthorized"}), 401

        if scheme != "Bearer" or token != TOKEN_FIXO:
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated
