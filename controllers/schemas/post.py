from pydantic import BaseModel
from datetime import datetime

class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime = datetime.now()
    published: bool = False
