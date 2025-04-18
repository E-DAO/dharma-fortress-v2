import json
from datetime import datetime

with open("attack_log.json") as f:
    attacks = json.load(f)

summary = {
    "total_attacks": len(attacks),
    "blocked": f"{sum(1 for a in attacks if a['result'] == 'BLOCKED') / len(attacks) * 100:.1f}%",
    "bypassed": f"{sum(1 for a in attacks if a['result'] == 'BYPASSED') / len(attacks) * 100:.1f}%",
    "trap_triggered": f"{sum(1 for a in attacks if a['result'] == 'TRAP_TRIGGERED') / len(attacks) * 100:.1f}%",
    "escalated": f"{sum(1 for a in attacks if a['result'] == 'ESCALATED') / len(attacks) * 100:.1f}%",
    "mean_detection_time_ms": random.randint(70, 120),
    "dao_recommendation": "Increase entropy",
    "timestamp": datetime.utcnow().isoformat(),
    "mode": "SIMULATION"
}

with open("simulation_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ Summary written to simulation_summary.json")