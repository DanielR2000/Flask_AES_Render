from flask import Flask, jsonify
from flask_talisman import Talisman
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Forzar HTTPS para todas las solicitudes
Talisman(app)  # Fuerza HTTPS

# Cargar la clave AES desde una variable de entorno
AES_KEY = os.getenv("AES_KEY")

# Verificar que la clave AES esté presente en las variables de entorno
if not AES_KEY:
    raise ValueError("Falta la clave AES en las variables de entorno")

# Crear un endpoint para obtener la clave AES
@app.route("/get-key", methods=["GET"])
def get_key():
    # Devuelve la clave AES en formato JSON
    return jsonify({"aes_key": AES_KEY}), 200

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
