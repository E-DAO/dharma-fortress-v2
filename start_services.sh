#!/bin/bash

echo ""
echo "🔁 Launching YinYang Engine Services..."
echo "-----------------------------------------"

# ✅ STEP 1: Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment activated."
else
    echo "❌ Virtual environment not found. Run: python3 -m venv venv && source venv/bin/activate"
    exit 1
fi

# ✅ STEP 2: Start Streamlit Operator Console
echo ""
echo "🧠 Starting Operator Console (Streamlit on :8501)..."
streamlit run app/interface/dashboard_console.py &

# ✅ STEP 3: Start FastAPI (Uvicorn) for Real-Time Input API
if [ -f "app/real_api.py" ]; then
    echo ""
    echo "⚖ Starting Real Input FastAPI API (:8000)..."
    uvicorn app.real_api:app --host 0.0.0.0 --port 8000 &
else
    echo "⚠️  app/real_api.py not found — skipping real-time API"
fi

# ✅ STEP 4: Start Core FastAPI App (Optional)
if [ -f "app/main.py" ]; then
    echo ""
    echo "🌐 Starting Core FastAPI App (:8000)..."
    uvicorn app.main:app --host 0.0.0.0 --port 8000 &
else
    echo "⚠️  app/main.py not found — skipping core app"
fi

# ✅ Final Message
echo ""
echo "✅ All systems active. Check your services:"
echo "------------------------------------------"
echo "🔗 Operator Console: http://localhost:8501"
echo "🔗 Real Input API:   http://localhost:8000/real-input"
echo "🔗 Core App:         http://localhost:8000 (if applicable)"
echo ""


