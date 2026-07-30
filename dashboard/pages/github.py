import streamlit as st
import plotly.express as px

from queries.github_queries import (
    get_top_languages,
    get_top_repositories,
    get_top_owners,
    get_language_statistics,
)

def show():

    st.title("🐙 GitHub Dashboard")

    languages = get_top_languages()

    repositories = get_top_repositories()

    owners = get_top_owners()

    statistics = get_language_statistics()
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Languages",
        len(statistics)
    )

    col2.metric(
        "Repositories",
        len(repositories)
    )

    col3.metric(
        "Owners",
        len(owners)
    )

    col4.metric(
        "Total Stars",
        int(repositories["stars"].sum())
    )
    st.subheader("Top Languages")

    fig = px.bar(
        languages,
        x="language_name",
        y="repository_count",
        title="Repositories by Language"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Top Repositories")

    st.dataframe(
        repositories,
        use_container_width=True
    )
    st.subheader("Top Owners")

    st.dataframe(
        owners,
        use_container_width=True
    )
    st.subheader("Language Statistics")

    st.dataframe(
        statistics,
        use_container_width=True
    )