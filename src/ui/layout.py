import streamlit as st
from google.genai.errors import APIError
from httpx2 import HTTPError, TimeoutException

from src.config import GEMINI_MODEL
from src.validation import validate_inputs


def build_dashboard(client) -> None:
    st.title("AI Career Roadmap & Skill Gap Finder")
    st.write(
        "Describe your current skills and target role to get an 8-week learning "
        "roadmap with skill gaps and portfolio project ideas."
    )

    with st.form("roadmap_form"):
        skills = st.text_area("Your current skills", placeholder="Python, SQL, ...")
        career = st.text_input("Target career or job role", placeholder="Data analyst")
        hours = st.number_input(
            "Learning hours per week", min_value=1, max_value=80, value=8
        )
        submitted = st.form_submit_button("Generate my roadmap")

    if not submitted or not validate_inputs(skills, career, hours):
        return

    prompt = (
        "Create a personalized career learning plan for someone targeting "
        f"{career}. Their current skills are: {skills}. They can study "
        f"{hours} hours per week.\n\n"
        "Include all of these sections in Markdown:\n"
        "## Skill gap analysis\n"
        "Compare the person's current skills with the target role. Identify "
        "strengths and the most important missing skills.\n\n"
        "## Personalized 8-week learning roadmap\n"
        "Give exactly eight clearly labeled weeks (Week 1 through Week 8). "
        "For each week, include a learning goal, relevant topics, and a "
        "hands-on task scaled to the available weekly study hours.\n\n"
        "## Three portfolio project recommendations\n"
        "Give exactly these three subsections: `### Project 1: [name]`, "
        "`### Project 2: [name]`, and `### Project 3: [name]`. For each, "
        "include a short description and the skills it demonstrates."
    )
    with st.spinner("Creating your roadmap..."):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )
        except APIError as error:
            api_error_message = (error.message or "").casefold()
            invalid_key = error.code in (401, 403) or (
                error.code == 400
                and (
                    "api key" in api_error_message
                    or "api_key_invalid" in api_error_message
                )
            )
            if invalid_key:
                st.error(
                    "Gemini rejected the API key or the key does not have "
                    "permission to use this model. Check the key in Streamlit "
                    "secrets."
                )
            elif error.code == 404:
                st.error(
                    f"Gemini model `{GEMINI_MODEL}` is unavailable for this "
                    "API key. Verify the model in the Gemini API model list."
                )
            elif error.code == 429:
                st.error(
                    "Gemini's request or quota limit was reached. Wait a bit "
                    "or review your Gemini API usage and billing limits."
                )
            elif error.code == 400:
                st.error(
                    "Gemini could not accept this request. Please review the "
                    "inputs and try again."
                )
            elif error.code >= 500:
                st.error(
                    "The Gemini service is temporarily unavailable. Please "
                    "try again shortly."
                )
            else:
                st.error(
                    f"Gemini returned an API error (HTTP {error.code}). "
                    "Please try again."
                )
            return
        except TimeoutException:
            st.error("The connection to Gemini timed out. Please try again.")
            return
        except HTTPError:
            st.error(
                "Could not connect to Gemini. Check your internet connection "
                "and try again."
            )
            return

    if not response.text:
        st.error("Gemini returned an empty response. Please try again.")
        return

    st.markdown(response.text)
