from flask import Flask, render_template, send_file, jsonify
import subprocess
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_simulation", methods=["POST"])
def run_simulation():
    subprocess.run(["python3", "simulate_attack.py"])
    subprocess.run(["python3", "postprocess_simulation.py"])
    subprocess.run(["python3", "generate_report.py"])
    return jsonify({"status": "success"})

@app.route("/get_summary", methods=["GET"])
def get_summary():
    if not os.path.exists("simulation_summary.json"):
        return jsonify({"error": "No summary found."}), 404
    with open("simulation_summary.json") as f:
        summary = json.load(f)
    return jsonify(summary)

@app.route("/download", methods=["GET"])
def download():
    return send_file("YinYang_Simulation_Report.pdf", 
as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5050)

