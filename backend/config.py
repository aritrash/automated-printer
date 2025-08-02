import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret")
    UPLOAD_FOLDER = os.path.join("instance", "uploaded_docs")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max file size
