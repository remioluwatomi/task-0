import os
from flask import Blueprint, jsonify
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def get_info():
    """Retrieve basic information.

    Returns a JSON response containing my email,
    current UTC timestamp, and GitHub repository URL.

    Returns:
        - dict: JSON response with the following keys:
            - email (str): Developer's contact email
            - current_datetime (str): Current UTC timestamp in ISO 8601 format
            - github_url (str): URL to the project's GitHub repository
        - int: HTTP status code 200 (OK)

    Example response:
        {
            "email": "hng@gmail.com",
            "current_datetime": "2025-01-29T14:30:45Z",
            "github_url": "https://github.com/username/repo"
        }
    """

    response = {
        "email": os.environ.get("MY_EMAIL"),
        "current_datetime": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "github_url": os.environ.get("GITHUB_REPO_URL")
    }
    return jsonify(response), 200
