#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt,
    get_jwt_identity
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from functools import wraps
import os

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY", "development-secret-change-me"
)

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Users with hashed passwords and assigned roles
users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    },
    "john": {
        "password": generate_password_hash("john123"),
        "role": "user"
    }
}


# -----------------------------
# BASIC AUTHENTICATION
# -----------------------------

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT AUTHENTICATION
# -----------------------------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]}
        )

        return jsonify({
            "access_token": access_token
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401


# -----------------------------
# JWT PROTECTED ROUTE
# -----------------------------

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()

    return jsonify({
        "message": "JWT Auth: Access Granted",
        "user": current_user
    }), 200


# -----------------------------
# ROLE-BASED ACCESS CONTROL
# -----------------------------

def role_required(required_role):
    def decorator(func):
        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()

            if claims.get("role") != required_role:
                return jsonify({
                    "error": "Access forbidden: insufficient permissions"
                }), 403

            return func(*args, **kwargs)

        return wrapper
    return decorator


# Admin-only route
@app.route("/admin-only")
@role_required("admin")
def admin_only():
    return jsonify({
        "message": "Welcome, Admin!"
    }), 200


# User-only route
@app.route("/user-only")
@role_required("user")
def user_only():
    return jsonify({
        "message": "Welcome, User!"
    }), 200


# -----------------------------
# HOME AND STATUS ROUTES
# -----------------------------

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
