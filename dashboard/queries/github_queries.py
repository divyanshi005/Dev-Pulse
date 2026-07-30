import pandas as pd

from config.database import database


def get_top_languages():
    query = """
    SELECT *
    FROM analytics.top_languages;
    """
    return pd.read_sql(query, database.engine)


def get_top_owners():
    query = """
    SELECT *
    FROM analytics.top_owners;
    """
    return pd.read_sql(query, database.engine)


def get_top_repositories():
    query = """
    SELECT *
    FROM analytics.top_repositories;
    """
    return pd.read_sql(query, database.engine)


def get_language_statistics():
    query = """
    SELECT *
    FROM analytics.language_statistics;
    """
    return pd.read_sql(query, database.engine)