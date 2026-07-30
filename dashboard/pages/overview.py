import streamlit as st

from queries.github_queries import (
    get_language_statistics,
)

from queries.stackexchange_queries import (
    get_top_questions,
)

def show():

    st.title("🚀 DevPulse")

    st.caption("Developer Intelligence Dashboard")

    language_df = get_language_statistics()

    question_df = get_top_questions()
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Languages",
            len(language_df)
        )

    with col2:
        st.metric(
            "Top Questions",
            len(question_df)
        )
    st.subheader("Top Languages")

    st.dataframe(language_df)
    st.subheader("Popular Stack Overflow Questions")

    st.dataframe(question_df)