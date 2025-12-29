from contextlib import asynccontextmanager
from typing import Union
from fastapi import FastAPI, Depends
from src.api.events import router as event_router
from sqlalchemy import text
from src.api.db.session import init_db
from src.api.events import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Hello World lifespan.........")
    # before app startup
    init_db()
    yield
    # some clean up here

app = FastAPI()
app.include_router(event_router, prefix='/api/events')


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}
