import os
import uuid
import qrcode
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload_bp', __name__)

# Paths and URLs
UPLOAD_FOLDER = os.path.join('shared', 'uploads')
QR_FOLDER = os.path.join('shared', 'qrcodes')
BASE_URL = "http://localhost:5000"  # Replace with Pi’s IP in prod

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(QR_FOLDER, exist_ok=True)

@upload_bp.route('/', methods=['POST'])  # <-- Notice the fix here!
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    unique_id = str(uuid.uuid4())
    saved_name = f"{unique_id}_{filename}"
    file_path = os.path.join(UPLOAD_FOLDER, saved_name)
    file.save(file_path)

    file_url = f"{BASE_URL}/files/{saved_name}"
    qr_path = os.path.join(QR_FOLDER, f"{unique_id}.png")

    qr_img = qrcode.make(file_url)
    qr_img.save(qr_path)

    return jsonify({
        'file_url': file_url,
        'qr_code_path': f"/qrcodes/{unique_id}.png"
    })
