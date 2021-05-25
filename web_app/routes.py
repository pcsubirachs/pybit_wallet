# current app ppints to config in app.py
from flask import Blueprint, jsonify, request, render_template, current_app
from bitcoin import *
from web_app.make_address import make_address
from web_app.make_address import bp

#
# ROUTING
#

this = Blueprint("this", __name__)

@this.route("/", methods=['POST', 'GET'])
def index():
    
    address = make_address()

    return render_template('PYBIT_index.html', address=address)

@this.route("/", methods=['POST', 'GET'])
def brain():
    #user input here
    phrase = request.form['user_phrase']
    # generate private key from input
    priv_key = sha256(phrase)
    # generate public key from your private key
    pub_key = privtopub(priv_key_brain)
    # then create a readable Bitcoin address
    brain = pubtoaddr(pub_key_brain)

    return render_template('PYBIT_index.html', brain=brain)

@this.route("/fknabt", methods=['POST', 'GET'])
def jinja():
    return render_template('PYBIT_fknabt.html')