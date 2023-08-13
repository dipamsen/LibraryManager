from flask import Flask, request, jsonify
import data as db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes in the app


@app.route("/")
def hello():
    return "Hello, Flask!"


@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.json
        query = data.get("q")
        args = data.get("args", [])

        if query is None:
            return jsonify({"error": 'Missing "q" in JSON data'}), 400

        result = db.Query(query, tuple(args))
        # Process the result if needed

        return jsonify({"result": result[0], "columns": result[1]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
