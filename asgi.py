import asyncio

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from main import start_consumer
from wsgi import app as flask_app

app = FastAPI()
loop = asyncio.get_event_loop()
app.mount("/v1", WSGIMiddleware(flask_app))


@app.on_event("startup")
async def startup_event():
    loop.create_task(start_consumer())


@app.get("/")
async def root():
    return {"message": "Hello, Fast API"}
