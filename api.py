from flask import Flask, request, jsonify
from precision_edao_engine import PrecisionEDAOEngine  # Import from separate file

app = Flask(__name__)
edao = PrecisionEDAOEngine()  # Create an instance of the engine

@app.route("/api/edao/gateway", methods=["POST"])
def edao_gateway():
    try:
        data = request.get_json()
        input_data = data.get("input_data", "")
        session_history = data.get("session_history", [])
        timestamps = data.get("timestamps", [])

        result = edao.process_request(input_data, session_history, timestamps)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
