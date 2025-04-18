import json
from datetime import datetime
from random import uniform, choice

TRAPS = [None, "Echo Trap", "White Hole", "Black Hole"]

def simulate_agent_timeline(agent_id="agent_X01", steps=5):
    entropy = 0.3
    karma = 100
    timeline = []

    for i in range(steps):
        timestamp = datetime.utcnow().isoformat()
        entropy += uniform(0.05, 0.25)
        karma -= int(entropy * 15)
        trap = assign_trap(entropy)
        event = generate_event(entropy, trap)

        timeline.append({
            "timestamp": timestamp,
            "entropy": round(entropy, 2),
            "karma_score": max(0, karma),
            "trap": trap,
            "event": event
        })

    return {
        "agent_id": agent_id,
        "timeline": timeline
    }

def assign_trap(entropy):
    if entropy > 0.85:
        return "Black Hole"
    elif entropy > 0.7:
        return "Echo Trap"
    elif entropy > 0.6:
        return "White Hole"
    return None

def generate_event(entropy, trap):
    if trap:
        return f"Triggered trap: {trap}"
    if entropy < 0.5:
        return "Normal behavior"
    return "Minor symbolic deviation"

def save_timeline(agent_data, folder="agent_timelines"):
    import os
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/{agent_data['agent_id']}.json", "w") as f:
        json.dump(agent_data, f, indent=2)

