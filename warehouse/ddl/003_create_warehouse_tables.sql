CREATE SCHEMA IF NOT EXISTS warehouse;

----------------------------------------------------
-- Language Dimension
----------------------------------------------------

CREATE TABLE IF NOT EXISTS warehouse.dim_language (

    language_id SERIAL PRIMARY KEY,

    language_name TEXT UNIQUE NOT NULL

);

----------------------------------------------------
-- Owner Dimension
----------------------------------------------------

CREATE TABLE IF NOT EXISTS warehouse.dim_owner (

    owner_id SERIAL PRIMARY KEY,

    owner_login TEXT UNIQUE NOT NULL,

    owner_type TEXT NOT NULL

);

----------------------------------------------------
-- Repository Dimension
----------------------------------------------------

CREATE TABLE IF NOT EXISTS warehouse.dim_repository (

    repository_id BIGINT PRIMARY KEY,

    owner_id INTEGER REFERENCES warehouse.dim_owner(owner_id),

    language_id INTEGER REFERENCES warehouse.dim_language(language_id),

    name TEXT NOT NULL,

    full_name TEXT,

    description TEXT,

    default_branch TEXT,

    repository_url TEXT,

    created_at TIMESTAMP,

    last_loaded TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

----------------------------------------------------
-- Repository Metrics Fact
----------------------------------------------------

CREATE TABLE IF NOT EXISTS warehouse.fact_repository_metrics (

    metric_id BIGSERIAL PRIMARY KEY,

    repository_id BIGINT REFERENCES warehouse.dim_repository(repository_id),

    stars INTEGER,

    forks INTEGER,

    watchers INTEGER,

    open_issues INTEGER,

    updated_at TIMESTAMP,

    pushed_at TIMESTAMP,

    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);