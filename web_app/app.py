import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from web_app.routes import this
from flask_qrcode import QRcode


load_dotenv()

def create_app():
    # initializing new flask app
    app = Flask(__name__)
    # extending app to QR code
    QRcode(app)
    # linking to routes.py page via the "routes" variable
    app.register_blueprint(this)
    
    return app