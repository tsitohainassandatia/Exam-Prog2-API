from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response

app = FastAPI()

#Question 1
@app.get('/ping')
def read_ping():
    return Response("pong")

#Question 2
@app.get('/home')
def read_home(): 
    with open("welcome.html", encoding="utf-8") as file:
        html_content = file.read()

    return Response(content=html_content, status_code=200, 
media_type="text/html")