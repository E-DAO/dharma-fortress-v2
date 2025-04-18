from datetime import datetime, timedelta

SESSIONS = {}

def create_session(route, ip, ttl=60):
    expires = datetime.utcnow() + timedelta(seconds=ttl)
    SESSIONS[route] = { "ip": ip, "expires": expires }

def validate_session(route, ip):
    session = SESSIONS.get(route)
    if not session:
        return False
    if session['ip'] != ip:
        return False
    if session['expires'] < datetime.utcnow():
        return False
    return True