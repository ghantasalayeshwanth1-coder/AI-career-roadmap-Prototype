import streamlit as st


def validate_inputs(skills: str, career: str, hours: int) -> bool:
    """Validate user inputs.

    Returns True if all inputs are acceptable, otherwise shows an error
    message via Streamlit and returns False.
    """
    if not skills.strip():
        st.error("Please enter at least one current skill.")
        return False
    if not career.strip():
        st.error("Please specify a target career or job role.")
        return False
    if hours <= 0:
        st.error("Learning hours per week must be a positive number.")
        return False
    return True
