from routes.planning_routes import planning_bp
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plan", methods=["POST"])
def plan_trip():
    data = request.json
    # For now, just echo back data
    return jsonify({"status": "received", "input": data})

if __name__ == "__main__":
    app.run(debug=True)
