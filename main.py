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

@app.route('/posts', methods=['POST'])
def create_posts():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"error": "Request body must be a list of post objects"}), 400

    processed_posts = []
    errors = []

    for item in data:
        required_fields = ["author", "title", "content", "creation_datetime"]
        if not all(field in item for field in required_fields):
            errors.append({"message": "Missing required fields in one or more post objects", "post": item})
            continue


        if not all(isinstance(item[field], str) for field in ["author", "title", "content"]):
            errors.append({"message": "Author, title, and content must be strings", "post": item})
            continue

        try:

            item['creation_datetime'] = datetime.fromisoformat(item['creation_datetime'].replace('Z', '+00:00'))
        except ValueError:
            errors.append({"message": "Invalid creation_datetime format. Use ISO 8601.", "post": item})
            continue

        processed_posts.append(item)

    if errors:
        return jsonify({"message": "Some posts had errors", "errors": errors, "processed_posts_count": len(processed_posts)}), 400

    return jsonify({"message": "Posts created successfully", "posts_received": len(processed_posts), "posts": processed_posts}), 201

if __name__ == '__main__':
    app.run(debug=True)