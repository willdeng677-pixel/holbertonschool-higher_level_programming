#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users in memory (no testing data)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse incoming JSON data
    data = request.get_json(silent=True)

    # Check for invalid JSON
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is provided
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user
    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
