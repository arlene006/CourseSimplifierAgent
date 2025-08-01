from flask import Flask, request, jsonify

app = Flask(__name__)

def simplify_content(input_text):
    # Right now this just echoes back. Later we will put your real agent/model logic here.
    return f"Simplified: {input_text}"

@app.route("/simplify", methods=["POST"])
def simplify():
    data = request.get_json(silent=True) or {}
    original = data.get("text", "")
    if not original:
        return jsonify({"error": "Give me some text in key 'text'"}), 400
    simplified = simplify_content(original)
    return jsonify({"original": original, "simplified": simplified})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


