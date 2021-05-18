# current app ppints to config in app.py
from flask import Blueprint, jsonify, request, render_template, current_app

#
# ROUTING
#

routes = Blueprint("routes", __name__)

# method decorators
# above our normal looking function, it specifies a route or url path
# each def needs to be unique for this to work
@routes.route("/")
def index():
    # return "Example"
    return render_template("index.html")

@routes.route("/about")
def about():
    return "About Me"