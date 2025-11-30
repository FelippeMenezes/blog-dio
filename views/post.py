from pydantic import BaseModel
from datetime import UTC, datetime

class PostOut(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False