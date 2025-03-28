from flask import Flask, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route("/get-key", methods=["GET"])
def get_key():
    aes_key = Fernet.generate_key()  # Genera una clave AES (256 bits)
    return jsonify({"aes_key": aes_key.decode()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
