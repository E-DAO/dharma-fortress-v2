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

txt
Copy
Edit
fastapi
uvicorn
jinja2
✅ Step 3: Project Structure Recap
Render will expect this layout:

arduino
Copy
Edit
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
✅ Step 4: Push to GitHub
From your project root:

bash
Copy
Edit
cd ~/github/yinyang-deception-engine
git add .
git commit -m "Deployment ready: structure + render config"
git push origin main
✅ Step 5: Deploy on https://render.com
Sign in / Create account

Click New Web Service

Connect to your repo

Render detects render.yaml

Click Deploy

🎉 Get a link like:

arduino
Copy
Edit
https://yinyang-deception.onrender.com/dashboard
