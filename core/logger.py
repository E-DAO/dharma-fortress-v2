import json
from datetime import datetime
import os

LOG_PATH = "data/deception_log.json"

def log_event(user_id, event_type, metadata):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "event": event_type,
        "details": metadata
    }

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    try:
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(log) + "\n")
    except Exception as e:
        print(f"[LOG ERROR] {e}")

def read_log():
    if not os.path.exists(LOG_PATH):
        return []

    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
        return [json.loads(line) for line in lines if line.strip()]
