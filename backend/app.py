from flask import Flask, send_from_directory
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configuration
    app.config.from_object("config.Config")

    # Ensure upload folder exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Register Blueprints
    from routes.upload import upload_bp
    from routes.status import status_bp

    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(status_bp, url_prefix='/status')

    # Static file routes
    @app.route('/')
    def home():
        return "Server is running! Use /status to check health."

    @app.route('/files/<filename>')
    def serve_file(filename):
        return send_from_directory('shared/uploads', filename)

    @app.route('/qrcodes/<filename>')
    def serve_qr(filename):
        return send_from_directory('shared/qrcodes', filename)

    return app
