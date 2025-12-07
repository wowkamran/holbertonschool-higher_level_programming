#!/usr/bin/python3
"""
A simple Flask API that supports GET and POST requests to manage users.
"""

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# In-memory users storage
users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Endpoint returning OK."""
    return "OK"


@app.route("/data")
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return the user object for the given username or 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request with JSON body."""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Save the new user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
