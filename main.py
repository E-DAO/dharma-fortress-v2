from fastapi import FastAPI, Request
from core.deception_core import process_session
from core.logger import read_log
from core.redemption import process_redemption
from core.karma import get_karma, get_all_karma

app = FastAPI()

# ────────────────────────────────────────
# 🔍 Risk Analysis Endpoint
# ────────────────────────────────────────
@app.post("/api/risk")
async def risk_endpoint(request: Request):
    data = await request.json()
    user_id = data.get("user_id")

    # 🛡️ Auto-ban logic
    karma = get_karma(user_id)
    if karma < 0.3:
        from core.logger import log_event
        log_event(user_id, "BANNED", {"karma": karma})
        return {
            "status": "banned",
            "message": "User karma too low. Access denied.",
            "karma": round(karma, 2)
        }

    # 🧠 If user passes karma check, process normally
    result = process_session(data)
    return result


# ────────────────────────────────────────
# ✅ Status Check
# ────────────────────────────────────────
@app.get("/status")
def status():
    return {"status": "online", "message": "Deception Engine ready"}

# ────────────────────────────────────────
# 📜 Deception Log Viewer
# ────────────────────────────────────────
@app.get("/log")
def get_logs():
    return read_log()

# ────────────────────────────────────────
# 🧩 Redemption Flow (Boost Karma)
# ────────────────────────────────────────
@app.post("/redeem")
async def redeem(request: Request):
    data = await request.json()
    user_id = data["user_id"]
    score = data["test_score"]
    result = process_redemption(user_id, score)
    return result

# ────────────────────────────────────────
# 🎫 Karma Score Lookup (Per User)
# ────────────────────────────────────────
@app.get("/karma/{user_id}")
def karma_for_user(user_id: str):
    score = get_karma(user_id)
    return {
        "user_id": user_id,
        "karma": round(score, 2),
        "status": (
            "trusted" if score >= 0.75 else
            "borderline" if score >= 0.5 else
            "at risk"
        )
    }

# ────────────────────────────────────────
# 📊 Karma Leaderboard (All Users)
# ────────────────────────────────────────
@app.get("/karma")
def karma_all():
    return get_all_karma()
