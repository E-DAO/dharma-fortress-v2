import json
import random
from datetime import datetime

ATTACK_TYPES = ["flashloan", "reentrancy", "impersonation", "overflow"]
RESULTS = ["BLOCKED", "BYPASSED", "TRAP_TRIGGERED", "ESCALATED"]

def generate_attack():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "attacker": f"0x{random.randint(10**7, 10**8):x}",
        "attack_type": random.choice(ATTACK_TYPES),
        "result": random.choices(
            RESULTS, weights=[0.3, 0.1, 0.5, 0.1], k=1
        )[0]
    }

def main():
    attacks = [generate_attack() for _ in range(10)]
    with open("attack_log.json", "w") as f:
        json.dump(attacks, f, indent=2)
    print("✅ Simulation complete. 10 entries saved to attack_log.json")

if __name__ == "__main__":
    main()