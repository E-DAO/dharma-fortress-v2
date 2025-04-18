def trigger_trap(user_id, trap_type="blackhole"):
    if trap_type == "blackhole":
        return {"status": "trap", "message": "You are in a recursive loop."}
    elif trap_type == "echozone":
        return {"status": "echo", "message": f"User {user_id}, your input is being echoed."}
    else:
        return {"status": "unknown", "message": "Unknown trap"}

