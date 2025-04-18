from core.timeline import simulate_agent_timeline, save_timeline

agent_id = "agent_Z03"
steps = 6

data = simulate_agent_timeline(agent_id, steps)
save_timeline(data)

