import pandas as pd

from config.database import database


def get_top_questions():
    query = """
    SELECT *
    FROM analytics.top_questions;
    """
    return pd.read_sql(query, database.engine)


def get_top_tags():
    query = """
    SELECT *
    FROM analytics.top_tags;
    """
    return pd.read_sql(query, database.engine)


def get_tag_statistics():
    query = """
    SELECT *
    FROM analytics.tag_statistics;
    """
    return pd.read_sql(query, database.engine)


def get_owner_statistics():
    query = """
    SELECT *
    FROM analytics.owner_statistics;
    """
    return pd.read_sql(query, database.engine)