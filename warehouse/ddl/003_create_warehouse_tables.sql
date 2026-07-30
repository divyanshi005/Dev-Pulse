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

    owner_name TEXT  NOT NULL,

    owner_type TEXT ,

    platform TEXT,
    UNIQUE (owner_name, platform)

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

    repository_id BIGINT UNIQUE REFERENCES warehouse.dim_repository(repository_id),

    stars INTEGER,

    forks INTEGER,

    watchers INTEGER,

    open_issues INTEGER,

    updated_at TIMESTAMP,

    pushed_at TIMESTAMP,

    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


----------------------------------------------------
-- Questions Dimensions
----------------------------------------------------


CREATE TABLE IF NOT EXISTS warehouse.dim_question(
    
    question_id BIGINT PRIMARY KEY,

    title TEXT NOT NULL,

    owner_id INTEGER REFERENCES warehouse.dim_owner(owner_id),

    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

----------------------------------------------------
-- Questions Metrics Fact
----------------------------------------------------


CREATE TABLE IF NOT EXISTS warehouse.fact_question_metrics(

    metric_id BIGSERIAL PRIMARY KEY,

    question_id BIGINT UNIQUE REFERENCES warehouse.dim_question(question_id),

    score INTEGER,

    answer_count INTEGER,

    view_count INTEGER,

    last_loaded TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

----------------------------------------------------
-- TAG Dimensions
----------------------------------------------------


CREATE TABLE IF NOT EXISTS warehouse.dim_tag(

    tag_id SERIAL PRIMARY KEY,

    tag_name TEXT UNIQUE NOT NULL

);

----------------------------------------------------
-- Bridge Table for Many-to-Many Relationship between Questions and Tags
----------------------------------------------------

CREATE TABLE IF NOT EXISTS warehouse.bridge_question_tag(

    question_id BIGINT REFERENCES warehouse.dim_question(question_id),

    tag_id INTEGER REFERENCES warehouse.dim_tag(tag_id),

    PRIMARY KEY (question_id, tag_id)

);