from flask import Blueprint, jsonify
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def get_info():
    return jsonify({
        
    })
