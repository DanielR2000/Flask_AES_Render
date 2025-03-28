from flask import Flask, jsonify
from flask_talisman import Talisman
import os

app = Flask(__name__)
Talisman(app)  # Fuerza HTTPS

# Cargar la clave AES desde una variable de entorno
AES_KEY = os.getenv("AES_KEY")

if not AES_KEY:
    raise ValueError("Falta la clave AES en las variables de entorno")

@app.route("/get-key", methods=["GET"])
def get_key():
    return jsonify({"aes_key": AES_KEY}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
