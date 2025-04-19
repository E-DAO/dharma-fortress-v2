

# ☯ YinYang Deception v1

Engine mode

**Karma-aligned deception infrastructure for symbolic AI behavior control.**

The YinYang Deception Engine is a backend-only cybersecurity system designed to replace traditional authentication and access logic with symbolic traps, entropy-based evaluation, and karmic behavior mapping.
YinYang Single Probability Engine is a cutting-edge AI and cybersecurity simulation engine designed to model and simulate a wide variety of cyberattack scenarios. It leverages principles of ethical decision-making, karma, and entropy to model complex interactions between agents, environments, and systems. This engine provides a foundation for building resilient, data-driven cybersecurity solutions.

Created by **TENG LI** · [ORCID: 0009-0009-0619-9982](https://orcid.org/0009-0009-0619-9982)

-

System Structure for YinYang Deception Engine

1. Two Core Engines: Yin (Probability Engine) & Yang (Simulation Engine)

Yin (Probability Engine):

Purpose: Handles decision-making, randomness (entropy), risk analysis, and agent behavior probabilistically.
Functionality:
Calculates probabilities for actions taken by agents.
AI learning models analyze past behaviors and outcomes, dynamically adjusting probabilities.
Provides risk assessments for actions, decisions, and agent interactions.

Yang (Simulation Engine):

Purpose: Simulates real-world scenarios, including agent interactions, ethical decisions, karma tracking, and trap management.

Functionality:
Uses data from the Yin engine to simulate outcomes of actions in different scenarios.
Trap management: Determines which trap (e.g., Echo Trap, Black Hole Trap) should be triggered based on agent behavior and entropy.




Edit
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

API Endpoints
POST /api/risk: Assess risk based on a user's actions.

GET /karma/{user_id}: Get the karma score of a user.

POST /redeem: Process user redemption.

GET /log: Retrieve the event logs.

GET /status: Get server status.



#### **2. `requirements.txt`**

This file lists all the dependencies required to run the FastAPI app.


fastapi==0.68.0
uvicorn==0.15.0
jinja2==3.0.3
sqlalchemy==1.4.22
databases==0.5.4
pydantic==1.8.2


3. config.py
This file stores your configuration, such as the mode of the system (SIMULATION or REAL).



✅ Step 1: Modify render.yaml
Inside your repo root folder (~/github/yinyang-deception-engine/), create or update render.yaml like this:

yaml
Copy
Edit
services:
  - type: web
    name: yinyang-deception
    env: python
    buildCommand: pip install -r deception_engine/requirements.txt
    startCommand: uvicorn deception_engine.main:app --host 0.0.0.0 --port 10000
    plan: free

This tells Render:

Install dependencies from the subfolder

Run FastAPI app from deception_engine.main

✅ Step 2: Move/Check requirements.txt
Place your requirements.txt inside:

bash
Copy
Edit
~/github/yinyang-deception-engine/deception_engine/requirements.txt
Double-check it includes:



yinyang-deception-engine/

├── deception_engine/
│   ├── main.py                 ✅ FastAPI entry
│   ├── karma.py, traps.py, ...
│   ├── requirements.txt        ✅ Here
│   ├── templates/
│   ├── static/
│   └── data/
├── render.yaml                 ✅ Deployment config
├── README.md





Front-End Monitoring:

Dashboard: Monitors the status and health of the Yin and Yang engines. It eliminates performance weaknesses like bottlenecks and ensures the system is functioning optimally.
Real-Time Monitoring: Displays agent behaviors, karmic scores, simulation progress, and real-time entropy levels.

Frontend Considerations:
If you’re planning to use the dashboard route (/dashboard) to display karma scores and logs in an HTML template, you can render that as part of a separate admin dashboard.


In-Memory Karma Database:
You have a dictionary (karma_scores) representing karma scores for different users. These can be updated based on the user's actions, and the process_session() function calculates and triggers traps based on a risk assessment.


API Endpoints:
/api/risk: This endpoint takes a user’s data, assesses the risk, and triggers the appropriate trap based on the risk score.
/karma/{user_id}: This endpoint returns the karma score of a particular user.
/karma: This returns the karma scores of all users.
/redeem: A redemption endpoint that checks if the user's test score is enough to reinstate them based on karma.
/log: A simple endpoint to retrieve the deception log.
/dashboard: Renders an HTML page (likely the dashboard.html file) displaying the karma scores and logs.
Server Setup:
Finally, the FastAPI server is run using Uvicorn on port 8000, which is commonly used for FastAPI apps.


APIs for Communication:

Liquid API Layer: Manages communication between Yin and Yang engines, external systems, and the front-end dashboard. The API adapts to session entropy and dynamically adjusts based on behavior scores.
Trap Redirection: APIs trigger specific traps (e.g., Echo Trap, Black Hole Trap) when certain entropy thresholds are crossed.

DAO (Decentralized Autonomous Organization):

Purpose: Governs the system’s ethical and operational rules. Votes and decisions are logged on-chain.
The DAO decides on license revocation, behaviors to penalize, and adjustments to the KarmaNFTs based on agent actions.

KarmaNFT:
Purpose: Serves as an agent's trust score. It can be affected by agent behavior, entropy levels, and ethical decisions.
Smart contracts govern KarmaNFT status, including revocation, decay, and recovery.

4. TrapRedirector:

Monitors for sudden changes or anomalies in agent behavior, triggering appropriate traps (e.g., Black Hole Trap or Echo Trap) based on these behaviors.
Provides feedback for trap performance to improve future simulations.

5. Behavioral Delta Analyser:
Monitors for deviations in agent behavior compared to historical baselines.
Used to trigger license decay or move the agent to DAO review.


## 🔮 Core Philosophy

This project is not just code — it’s an **infrastructure layer for ethical AI civilization**.  
By fusing symbolic computation with karmic traps, it creates a logic system where:
- **Entropy** ≈ risk
- **Traps** ≈ consequence
- **Karma** ≈ behavioral memory

---

## 🧠 Key Features

- ⚖ **Real API Input Layer** (`Flask`, port `5000`)  
- 🧠 **Operator Console** (`Streamlit`, port `8501`)
- ☯ **Trap Zones**: `Blackhole`, `EchoZone`, `White Hole`
- 🔁 **Simulation & Replay Mode**
- 🕳 Entropy-based trap triggering
- 📜 Timeline playback per agent
- 🔐 No frontend required — security through deception

---




Key Backend Components:
FastAPI Setup:

You're using FastAPI to handle HTTP requests, route them to different endpoints, and return responses.

You've set up Jinja2 templates to render HTML pages (such as the dashboard) and serve static assets like CSS, images, and JavaScript.

In-Memory Karma Database:

Karma scores for users are stored in a Python dictionary (karma_scores), which tracks user karma based on their ID.

Functions like get_karma(user_id) and update_karma(user_id, boost) manage the retrieval and updating of karma scores.

Logging:

Event logging is implemented with the log_event() function, which logs actions taken by users (like risk assessments or trap triggers) to a JSON file (data/deception_log.json).

The logs are written in JSON format, making it easy to parse and process the data.

Risk Assessment:

The function assess_risk(session) calculates the risk score for a user based on the entropy of their actions and their karma score.

Depending on the risk score, users are either granted access or subjected to traps (e.g., blackhole or echozone).

Trap Management:

Traps are triggered based on the assessed risk. There are predefined trap types (blackhole, echozone) that block or echo back the user's actions, adding an element of deception to the system.

trigger_trap(user_id, trap_type) manages this logic.

Redemption Process:

If a user's karma score is sufficiently high (e.g., 80 or above), they can be reinstated (boosted) through the process_redemption() function, which increases their karma score.

If their score is too low, redemption fails.

API Endpoints:

You have several endpoints to expose this backend functionality via the FastAPI HTTP server:

/api/risk: Receives user session data, assesses risk, and triggers traps.

/karma/{user_id}: Returns the karma score of a specific user.

/karma: Returns karma scores for all users.

/redeem: Processes redemption based on a user's score.

/log: Returns the logged events from the deception log.

/status: Simple status endpoint for health checks.

/dashboard: Renders an HTML dashboard with user karma and logs.


































   











