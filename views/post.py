from pydantic import BaseModel
from datetime import UTC, datetime

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime | None
