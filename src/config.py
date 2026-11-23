import streamlit as st
import google.generativeai as genai


def get_gemini_client():
    """Initialise and return a Gemini client.
    Expects the API key in `st.secrets["gemini"]["api_key"]`.
    Raises a Streamlit error if not found.
    """
    try:
        api_key = st.secrets["gemini"]["api_key"]
    except Exception:
        st.error(
"Gemini API key not found. Please add it to `.streamlit/secrets.toml` as:\n"
"```toml\n"
"[gemini]\n"
'api_key = "YOUR_GEMINI_API_KEY"\n'
"```"
        )
        st.stop()
    # Initialise the client (once per session)
    genai.configure(api_key=api_key)
    # Return a model object; we can reuse the same model for multiple calls.
    return genai.GenerativeModel('gemini-1.5-flash')
