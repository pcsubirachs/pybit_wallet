# current app ppints to config in app.py
from flask import Blueprint, jsonify, request, render_template, current_app
from bitcoin import *
from web_app.make_address import make_address

#
# ROUTING
#

this = Blueprint("this", __name__)

@this.route("/", methods=['POST', 'GET'])
def index():
    
    address = make_address()

    return render_template('index.html', address=address)
