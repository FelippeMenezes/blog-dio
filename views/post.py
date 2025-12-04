from pydantic import BaseModel
from datetime import UTC, datetime

class PostOut(BaseModel):
    title: str
    content: str
    published_at: datetime | None
