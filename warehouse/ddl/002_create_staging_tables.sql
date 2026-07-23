CREATE TABLE IF NOT EXISTS staging.github_repositories (

    repository_id       BIGINT PRIMARY KEY,

    name                TEXT NOT NULL,

    full_name           TEXT NOT NULL,

    owner_login         TEXT NOT NULL,

    owner_type          TEXT,

    description         TEXT,

    language            TEXT,

    stars               INTEGER,

    forks               INTEGER,

    watchers            INTEGER,

    open_issues         INTEGER,

    default_branch      TEXT,

    is_private          BOOLEAN,

    repository_url      TEXT,

    created_at          TIMESTAMP,

    updated_at          TIMESTAMP,

    pushed_at           TIMESTAMP,

    raw_ingested_at     TIMESTAMP NOT NULL
);