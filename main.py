from fastapi import FastAPI
from starlette.responses import Response
from starlette.responses import request, jsonify
from datetime import datetime

app = FastAPI()

@app.route('/ping', methods=['GET'])
def ping():
    return Response("pong", mimetype='text/plain', status=200)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

@app.route('/home', methods=['GET'])
def home():
    html_content = "<h1>Welcome home!</h1>"
    return Response(html_content, mimetype='text/html', status=200)

if __name__ == '__main__':
    app.run(debug=True)

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