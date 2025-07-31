from fastapi import FastAPI
from starlette.responses import Response
from starlette.responses import Flask, request, jsonify
from datetime import datetime

app = FastAPI()

@app.route('/ping', methods=['GET'])
def ping():
    return Response("pong", mimetype='text/plain', status=200)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

