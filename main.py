from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response

app = FastAPI()

@app.get('/ping')
def read_ping():
    return Response("pong")

