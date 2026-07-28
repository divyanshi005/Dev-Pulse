from dataclasses import dataclass
from datetime import datetime


@dataclass
class Question:
    question_id: int
    title: str
    owner_name: str | None
    score: int
    answer_count: int
    view_count: int
    creation_date: datetime
    tags: list[str]