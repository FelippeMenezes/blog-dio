from contextlib import asynccontextmanager

from controllers import post
from database import database, metadata, engine
from fastapi import FastAPI

@asynccontextmanager
async def applifespan(app: FastAPI):
    from models.post import posts #noqa
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=applifespan)
app.include_router(post.router)










@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield

