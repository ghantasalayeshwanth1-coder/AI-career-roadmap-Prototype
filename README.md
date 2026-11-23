# Project: AI Career Roadmap & Skill Gap Finder

A Streamlit app that uses the Gemini API to analyze a student's current skills, identify gaps for a target career, and generate an 8‑week learning roadmap with portfolio project suggestions.

## Quickstart
```bash
# 1. Create a virtual environment if you do not already have one
py -m venv .venv

# 2. Install the project dependencies (Windows)
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# 3. Store your Gemini API key in .streamlit/secrets.toml

# 4. Run the app
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

## Deploy to Streamlit Community Cloud

1. Publish this project to a GitHub repository. Do not upload `.streamlit/secrets.toml` or any API keys.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app and select the repository, branch, and `streamlit_app.py` as the main file.
3. In the app's **Settings → Secrets**, add the following TOML using your own Gemini API key:

   ```toml
   [gemini]
   api_key = "YOUR_GEMINI_API_KEY"
   ```

4. Save the settings and deploy. The app reads the key from `st.secrets["gemini"]["api_key"]`; the cloud deployment uses the Cloud Secrets setting and does not need your local secrets file.

## Project Structure
```
streamlit_app.py         # Streamlit Cloud main file
requirements.txt         # Python dependencies
src/
├─ config.py             # Load API key from Streamlit secrets
├─ validation.py         # Validate user input
└─ ui/
   └─ layout.py          # Render the app UI and request a roadmap
.streamlit/
└─ secrets.toml          # Local secrets only; excluded from Git
```

## Notes
- Locally, store the Gemini API key in `.streamlit/secrets.toml` using the same TOML structure shown above.
- Never commit API keys or secrets. `.streamlit/secrets.toml`, local environment files, virtual environments, and private key files are ignored by Git.

---
*Designed for college‑level AI prototypes – clean, modular, and easy to run.*