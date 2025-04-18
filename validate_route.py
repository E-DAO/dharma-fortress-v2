from session_store import validate_session
from trap_monitor import log_trap

def handle_route(route, request_ip, user_agent):
    if validate_session(route, request_ip):
        return { "status": "authorized" }, 200
    else:
        log_trap(route, request_ip, user_agent)
        return { "status": "trap_triggered" }, 403