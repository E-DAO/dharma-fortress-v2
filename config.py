# config.py

"""
YinYang Deception Engine — Core Configuration File
This controls the system-wide mode and future expansion flags.
"""

# ⚙️ Engine Mode Selector
# Options:
# - "SIMULATION": Use fake agents, synthetic data, operator testing
# - "REAL": Handle live payloads, log actual agent behavior
ENGINE_MODE = "SIMULATION"

# ✅ Feature Flags (future expansion)
ENABLE_DAO_GOVERNANCE = True         # Toggle DAO-based voting
LOG_TRAP_EVENTS = True               # Whether to log trap assignments
ENABLE_KARMA_NFT_TRACKING = True     # Use KarmaNFT logic for agent recovery
USE_PROBABILITY_ENGINE = True        # Core trust/entropy evaluator
SECURE_MODE = False                  # Lock down all traps in irreversible mode

# Optional: Path Aliases
SIM_LOG_PATH = "simulation_sessions/"
REAL_LOG_PATH = "real_events/"

