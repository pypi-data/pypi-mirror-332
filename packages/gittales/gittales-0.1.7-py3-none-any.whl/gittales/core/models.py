from datetime import datetime

from pydantic import BaseModel


class Commit(BaseModel):
    commit_hash: str
    author: str
    message: str
    date: datetime
    files: int


class Repository(BaseModel):
    name: str
    path: str


class ActivityEntry(BaseModel):
    start_time: datetime
    end_time: datetime
    duration_minutes: float
    commit: Commit
