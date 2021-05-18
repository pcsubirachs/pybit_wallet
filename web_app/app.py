import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from web_app.routes import routes

load_dotenv()

# database url as an environment variable
# DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

# if we invoke this from somehwere else 
# we will be able to use the function
def create_app():
    # initializing new flask app
    app = Flask(__name__)

    # not necessary to create this database beforehand
    # this will create the database for us and will create tables inside of it
    # configure the app and tell it which database to use
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testapp.db"
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    # importing models.py database class tables
    # links to __init__file which calls on create app to run
    #db.init_app(app)
    #migrate.init_app(app, db)

    # linking to routes.py page via my_routes variable
    app.register_blueprint(routes)
    
    return app