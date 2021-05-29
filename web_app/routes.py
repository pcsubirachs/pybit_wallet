# current app ppints to config in app.py
from flask import Blueprint, jsonify, request, render_template, current_app
from bitcoin import *
from web_app.make_address import make_address
from web_app.make_address import bp
from web_app.create_btc_wallet import create_wallet
import requests
from bs4 import BeautifulSoup

#
# ROUTING
#

this = Blueprint("this", __name__)

@this.route("/", methods=['POST', 'GET'])
def index():

    # generate private key
    private_key = random_key()
    # convert private key to public key
    public_key = privtopub(private_key)
    # then, create a readable Bitcoin address
    address = pubtoaddr(public_key)

    return render_template('index.html', private_key=private_key, public_key=public_key, address=address)

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

    return render_template('index.html', private_key=private_key, public_key=public_key, brain=brain)

@this.route("/test", methods=['POST','GET'])
def test():

    cw = create_wallet()

    seed=cw[0] 
    private_key=cw[1]
    public_key=cw[2] 
    address=cw[3]

    #return render_template('test.html', message = ("Yooo: " + seed + private_key + public_key + address))
    return render_template('test.html', seed=seed, private_key=private_key, public_key=public_key, address=address)

@this.route("/fknabt", methods=['POST', 'GET'])
def jinja():
    return render_template('PYBIT_fknabt.html')