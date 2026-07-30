import streamlit as st
from pages.overview import show as overview_page
from pages.github import show as github_page
from pages.stackexchange import show as stackexchange_page
st.set_page_config(
    page_title="DevPulse",
    page_icon="📊",
    layout="wide",
)

st.title("📊 DevPulse")

page = st.sidebar.selectbox(
    "Choose Dashboard",
    [
        "Overview",
        "GitHub",
        "Stack Exchange"
    ]
)

st.write(page)
if page == "Overview":
    overview_page()

elif page == "GitHub":
    github_page()

elif page == "Stack Exchange":
    stackexchange_page()