from core.karma import get_karma

def calculate_entropy(actions):
    return sum(actions) / len(actions) if actions else 0

def assess_risk(session):
    entropy = calculate_entropy(session["actions"])
    karma = session.get("karma", get_karma(session["user_id"]))  # Optional manual override
    risk_score = (entropy * 0.6) + ((1 - karma) * 0.4)
    return risk_score

