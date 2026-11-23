import streamlit as st
from google import genai
from streamlit.errors import StreamlitSecretNotFoundError

GEMINI_MODEL = "gemini-3.6-flash"


def get_gemini_client() -> genai.Client:
    """Create a Gemini client using the key in Streamlit secrets."""
    try:
        api_key = st.secrets["gemini"]["api_key"]
    except (KeyError, StreamlitSecretNotFoundError, TypeError):
        st.error(
            "Gemini API key not found. Add it to `.streamlit/secrets.toml` "
            "or the Streamlit Cloud Secrets settings using:\n"
            "```toml\n"
            "[gemini]\n"
            'api_key = "YOUR_GEMINI_API_KEY"\n'
            "```"
        )
        st.stop()
    if not isinstance(api_key, str) or not api_key.strip():
        st.error("The Gemini API key in Streamlit secrets is empty or invalid.")
        st.stop()

    return genai.Client(api_key=api_key)
