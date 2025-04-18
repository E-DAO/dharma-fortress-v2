from flask import Flask, render_template, request, redirect
import requests
import json
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")

FASTAPI_URL = "http://localhost:8000"  # your deception engine

@app.route("/")
def dashboard():
    try:
        karma_data = requests.get(f"{FASTAPI_URL}/karma").json()
        logs = requests.get(f"{FASTAPI_URL}/log").json()
    except Exception as e:
        karma_data = {}
        logs = [{"timestamp": "N/A", "event": "ERROR", "details": str(e)}]

    return render_template("dashboard.html", users=karma_data, logs=logs)

@app.route("/simulate", methods=["POST"])
def simulate():
    user_id = request.form["user_id"]
    actions = [int(x.strip()) for x in request.form["actions"].split(",")]
    try:
        result = requests.post(f"{FASTAPI_URL}/api/risk", json={
            "user_id": user_id,
            "actions": actions
        }).json()
    except Exception as e:
        result = {"error": str(e)}

    return render_template("result.html", result=result)

@app.route("/traps")
def trap_logs():
    logs = []
    if os.path.exists("trap_log.json"):
        try:
            with open("trap_log.json", "r") as f:
                logs = json.load(f)
        except Exception as e:
            logs = [{"timestamp": "N/A", "ip": "-", "event": "Error", "details": str(e)}]
    return render_template("trap_logs.html", logs=logs)

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_ENV") == "development"
    app.run(debug=debug_mode, port=5000)
