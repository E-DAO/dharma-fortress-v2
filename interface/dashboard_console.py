import streamlit as st
import json
import os
import subprocess
from PIL import Image

# Load config mode
from config import ENGINE_MODE

st.set_page_config(page_title="☯ YinYang Deception Console", layout="wide")

# Top bar + logo
st.markdown(
    """
    <style>
    .deploy-button {
        position: absolute;
        top: 1.5rem;
        right: 2rem;
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header + Deploy button
col1, col2 = st.columns([0.85, 0.15])
with col1:
    st.title("☯ YinYang Deception Engine – Operator Console")
with col2:
    if st.button("🛰 Deploy"):
        with open("config.py", "w") as f:
            f.write('ENGINE_MODE = "REAL"\n')
        st.success("🚀 Deployed: Engine now running in REAL mode.")

st.markdown(f"**🔄 Current Mode:** `{ENGINE_MODE}`")

# ======= Simulation Trigger =======
st.header("🎯 Run Simulation (Test Agent)")
if ENGINE_MODE == "SIMULATION":
    if st.button("Run Simulated Attack"):
        result = subprocess.run(["python3", "simulate_attack.py"], capture_output=True, text=True)
        st.text(result.stdout)
else:
    st.warning("Simulation mode is disabled. Switch to SIMULATION in config.py to run tests.")

# ======= View Simulation Logs =======
st.header("📄 Simulation Sessions")
sim_folder = "simulation_sessions"
if os.path.exists(sim_folder):
    sims = os.listdir(sim_folder)
    selected_sim = st.selectbox("Select session", sims)
    if selected_sim:
        with open(os.path.join(sim_folder, selected_sim)) as f:
            st.json(json.load(f))
else:
    st.info("No simulation logs found.")

# ======= View Real Input Logs =======
st.header("🧠 Real Agent Input Logs")
real_folder = "real_events"
if os.path.exists(real_folder):
    reals = os.listdir(real_folder)
    selected_real = st.selectbox("Select real input", reals)
    if selected_real:
        with open(os.path.join(real_folder, selected_real)) as f:
            st.json(json.load(f))
else:
    st.info("No real input logs found.")

# ======= Agent Timeline Viewer =======
st.header("🔮 Agent-Time Timeline Viewer")
timeline_folder = "agent_timelines"
if os.path.exists(timeline_folder):
    timelines = os.listdir(timeline_folder)
    selected_timeline = st.selectbox("Select agent timeline", timelines)
    if selected_timeline:
        with open(os.path.join(timeline_folder, selected_timeline)) as f:
            data = json.load(f)
            st.subheader(f"Agent: {data['agent_id']}")
            for entry in data["timeline"]:
                st.markdown(f"""
                **🕒 {entry['timestamp']}**  
                - Entropy: `{entry['entropy']}`  
                - Karma Score: `{entry['karma_score']}`  
                - Trap: `{entry['trap'] or 'None'}`  
                - Event: *{entry['event']}*
                """)
else:
    st.info("No timelines found. Run timeline simulation first.")

