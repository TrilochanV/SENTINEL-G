"""
SENTINEL-G — Real-Time AML & Cyber-Forensic Intelligence Platform
Flask application entry point.
"""
from flask import Flask, send_from_directory
from security.cors import configure_cors
from security.headers import apply_security_headers
from security.request_guard import install_request_guard
from security.rate_limit import install_rate_limiter
from routes.api import api
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")
configure_cors(app)
apply_security_headers(app)
install_request_guard(app)
install_rate_limiter(app)

# Register API blueprint
app.register_blueprint(api)

# SENTINEL-G Phase 2 detection services. Legacy routes remain untouched during migration.
from repositories.memory import InMemoryStateRepository
from services.transaction_service import TransactionDetectionService
state_repository = InMemoryStateRepository()
transaction_detection_service = TransactionDetectionService(repository=state_repository)



@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/<path:path>")
def serve_static(path):
    if os.path.exists(os.path.join("static", path)):
        return send_from_directory("static", path)
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    print("=" * 60)
    print("  [SENTINEL-G] AML & Cyber-Forensic Intelligence Platform")
    port = int(os.environ.get("PORT", "5000"))
    print(f"  Sentinel-G API: http://localhost:{port}")
    print("=" * 60)
    app.run(debug=os.environ.get("SENTINEL_DEBUG", "false").lower() == "true", host="0.0.0.0", port=port)
