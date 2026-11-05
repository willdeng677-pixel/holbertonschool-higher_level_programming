#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users in memory
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
    # Get JSON data from the request
    data = request.get_json(silent=True)

    # Check for invalid JSON
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    # Check for missing username
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to dictionary
    users[username] = data

    # Return confirmation
    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 200


if __name__ == "__main__":
    app.run()
