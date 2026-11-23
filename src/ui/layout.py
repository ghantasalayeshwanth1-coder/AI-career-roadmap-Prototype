import streamlit as st

from src.validation import validate_inputs


def build_dashboard(client):
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
        "Create a practical 8-week learning roadmap for someone targeting "
        f"{career}. Their current skills are: {skills}. They can study "
        f"{hours} hours per week. Identify the most important skill gaps, "
        "give weekly learning goals and hands-on tasks, and suggest portfolio "
        "projects. Format the response with clear Markdown headings and lists."
    )
    with st.spinner("Creating your roadmap..."):
        response = client.generate_content(prompt)

    st.markdown(response.text)
