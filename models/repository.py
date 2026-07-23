from dataclasses import dataclass
from datetime import datetime


@dataclass
class Repository:
    repository_id: int

    name: str
    full_name: str

    owner_login: str
    owner_type: str

    description: str | None

    language: str | None

    stars: int
    forks: int
    watchers: int
    open_issues: int

    default_branch: str

    is_private: bool

    repository_url: str

    created_at: datetime
    updated_at: datetime
    pushed_at: datetime

    raw_ingested_at: datetime