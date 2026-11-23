# Streamlit app entry point
import streamlit as st
from src.config import get_gemini_client
from src.ui.layout import build_dashboard

st.set_page_config(page_title="AI Career Roadmap & Skill Gap Finder", layout="centered")

# Load Gemini client (will raise if key missing)
client = get_gemini_client()

# Build the full UI – the function handles inputs, API calls, and result rendering
build_dashboard(client)
