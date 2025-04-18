def get_karma(user_id):
    fake_scores = {
        "0xabc": 0.9,
        "0xdef": 0.4,
        "0x999": 0.1
    }
    return fake_scores.get(user_id, 0.5)
# core/karma.py

# Simulated karma database (in-memory)
karma_scores = {
    "0xabc": 0.9,
    "0xdef": 0.4,
    "0x999": 0.1
}

def get_karma(user_id):
    return karma_scores.get(user_id, 0.5)

def update_karma(user_id, boost=0.1):
    current = karma_scores.get(user_id, 0.5)
    new_score = min(current + boost, 1.0)
    karma_scores[user_id] = new_score
    return new_score
def get_all_karma():
    return karma_scores



