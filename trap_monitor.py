import json
from datetime import datetime

def log_trap(route, ip, user_agent):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": ip,
        "guessed_route": route,
        "user_agent": user_agent
    }
    with open("trap_logs.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")