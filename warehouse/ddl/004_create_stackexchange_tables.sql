CREATE TABLE staging.stackexchange_questions (
    question_id BIGINT PRIMARY KEY,
    title TEXT NOT NULL,
    owner_name TEXT,
    score INTEGER,
    answer_count INTEGER,
    view_count INTEGER,
    creation_date TIMESTAMP,
    tags TEXT[],
    raw_ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);