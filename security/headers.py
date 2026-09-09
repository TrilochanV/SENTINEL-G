from flask import request

SECURITY_HEADERS={"X-Content-Type-Options":"nosniff","X-Frame-Options":"DENY","Referrer-Policy":"strict-origin-when-cross-origin","Permissions-Policy":"camera=(), microphone=(), geolocation=(), payment=(), usb=()","Cross-Origin-Opener-Policy":"same-origin"}
def apply_security_headers(app):
 @app.after_request
 def add_headers(response):
  for key,value in SECURITY_HEADERS.items(): response.headers.setdefault(key,value)
  if request.is_secure or app.config.get("FORCE_HSTS",False): response.headers.setdefault("Strict-Transport-Security","max-age=31536000; includeSubDomains")
  response.headers.setdefault("Content-Security-Policy","default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self';")
  return response
