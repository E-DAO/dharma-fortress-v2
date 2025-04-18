# real_api.py

from flask import Flask, request, jsonify
from config import ENGINE_MODE
from core.deception_core import handle_real_payload

app = Flask(__name__)

@app.route("/real-input", methods=["POST"])
def receive_real_input():
    if ENGINE_MODE != "REAL":
        return jsonify({"error": "Engine not in REAL mode"}), 403

    payload = request.json
    trap_result = handle_real_payload(payload)
    return jsonify({"result": trap_result}), 200

if __name__ == "__main__":
    app.run(port=5000)

