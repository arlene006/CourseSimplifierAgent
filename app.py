from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Course Simplifier Agent is running!"})

# TODO: Replace the above with your actual agent/model integration logic.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

