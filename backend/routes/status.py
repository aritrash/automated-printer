from flask import Blueprint, jsonify

status_bp = Blueprint('status_bp', __name__)

@status_bp.route('/', methods=['GET'])  # Fixed relative route
def status():
    return jsonify({
        "status": "OK",
        "message": "Backend server is running!",
        "uptime": "coming_soon"
    })
