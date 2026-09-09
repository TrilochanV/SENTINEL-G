import os
from flask import request,jsonify
MAX_BODY_BYTES=int(os.getenv("MAX_REQUEST_BYTES","1048576"))
def install_request_guard(app):
 @app.before_request
 def guard_request():
  if request.content_length and request.content_length>MAX_BODY_BYTES: return jsonify({"error":"request_too_large"}),413
