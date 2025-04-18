import streamlit as st
import requests

# FastAPI backend URL
API_BASE_URL = "http://127.0.0.1:8000"  # Make sure this is the correct URL

def get_karma(user_id):
    response = requests.get(f"{API_BASE_URL}/karma/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to retrieve karma.")
        return None

# UI - Karma Scores
st.title("☯ YinYang Deception Engine - Operator Console")
user_id = st.text_input("Enter User ID:")
if user_id:
    karma_data = get_karma(user_id)
    if karma_data:
        st.write(f"User ID: {karma_data['user_id']}")
        st.write(f"Karma: {karma_data['karma']}")
        st.write(f"Status: {karma_data['status']}")

