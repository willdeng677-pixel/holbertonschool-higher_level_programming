from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users in memory
users = {}


# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# Return all usernames
@app.route("/data", methods=["GET"])
def get_users():
    return jsonify(list(users.keys()))


# Check API status
@app.route("/status", methods=["GET"])
def status():
    return "OK"


# Return a specific user's information
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


# Add a new user
@app.route("/add_user", methods=["POST"])
def add_user():

    # Check whether the request contains valid JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check whether username is provided
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check whether username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the complete user object
    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
