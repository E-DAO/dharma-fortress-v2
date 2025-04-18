from core.karma import update_karma
from core.logger import log_event

def process_redemption(user_id, score):
    if score >= 80:
        new_karma = update_karma(user_id, boost=0.2)
        log_event(user_id, "REINSTATED", {"new_karma": new_karma})
        return {"status": "reinstated", "karma": new_karma}
    else:
        log_event(user_id, "REDEEM_FAILED", {"score": score})
        return {"status": "failed", "message": "Redemption score too low"}

