import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from web_app.routes import this

load_dotenv()

def create_app():
    # initializing new flask app
    app = Flask(__name__)

    # linking to routes.py page via the "routes" variable
    app.register_blueprint(this)
    
    return app