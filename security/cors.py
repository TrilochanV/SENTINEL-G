import os
from flask_cors import CORS
def configure_cors(app):
 origins=[o.strip() for o in os.getenv("CORS_ORIGINS","http://localhost:3000,http://localhost:5000").split(",") if o.strip()]
 CORS(app,resources={r"/api/*":{"origins":origins}},methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"],allow_headers=["Content-Type","Authorization"],supports_credentials=False,max_age=600)
