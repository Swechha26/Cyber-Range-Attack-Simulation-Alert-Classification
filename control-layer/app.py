from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/difficulty")
def difficulty():
    level = request.args.get("level", default="1")
    return jsonify(difficulty=level, message="Difficulty updated")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
