import os
try:
 from flask_limiter import Limiter
 from flask_limiter.util import get_remote_address
except ImportError: Limiter=None
def install_rate_limiter(app):
 if Limiter is None:
  app.logger.warning("flask-limiter not installed; rate limiting disabled"); return None
 return Limiter(key_func=get_remote_address,app=app,default_limits=[os.getenv("RATE_LIMIT_DEFAULT","120 per minute")],storage_uri=os.getenv("RATE_LIMIT_STORAGE_URI","memory://"))
