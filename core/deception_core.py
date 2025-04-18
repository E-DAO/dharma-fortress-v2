# core/deception_core.py

from core.probability import assess_risk
from core.trap import trigger_trap
from core.karma import get_karma  # Optional for expansion
from core.logger import log_event
from config import ENGINE_MODE

# 🧠 Main logic for symbolic risk assessment & trap assignment
def process_session(session):
    user_id = session["user_id"]
    actions = session.get("actions", [])

    # Step 1: Assess symbolic entropy / misuse probability
    risk = assess_risk(session)

    # Step 2: Decide and trigger trap route
    if risk > 0.75:
        log_event(user_id, "TRAP", {"risk": risk, "engine": ENGINE_MODE})
        return trigger_trap(user_id, "blackhole")

    elif risk > 0.55:
        log_event(user_id, "ECHOZONE", {"risk": risk, "engine": ENGINE_MODE})
        return trigger_trap(user_id, "echozone")

    else:
        log_event(user_id, "PASS", {"risk": risk, "engine": ENGINE_MODE})
        return {"status": "pass", "message": "Access granted"}

# 🔁 Used by real_api.py to handle live payloads
def handle_real_payload(payload):
    return process_session(payload)

# 🧪 Simulation wrapper (for local simulations or tests)
def run_deception_engine(simulated_session):
    log_event(simulated_session["user_id"], "SIM_RUN", {"mode": ENGINE_MODE})
    return process_session(simulated_session)
