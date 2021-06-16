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
    """
    # generate private key
    private_key = random_key()
    # convert private key to public key
    public_key = privtopub(private_key)
    # then, create a readable Bitcoin address
    address = pubtoaddr(public_key)

    return render_template('index.html', private_key=private_key, public_key=public_key, address=address)
    """
    cw = create_wallet()

    seed=cw[0] 
    private_key=cw[1]
    public_key=cw[2] 
    address=cw[3]

    #return render_template('test.html', message = ("Yooo: " + seed + private_key + public_key + address))
    return render_template('index.html', seed=seed, private_key=private_key, public_key=public_key, address=address)

@this.route("/brain", methods=['POST', 'GET'])
def brain():

    #user input here
    phrase = request.form['user_phrase']
    # generate private key from input
    priv_key_brain = sha256(phrase)
    # generate public key from your private key
    pub_key_brain = privtopub(priv_key_brain)
    # then create a readable Bitcoin address
    add_brain = pubtoaddr(pub_key_brain)

    return render_template('index.html', phrase=phrase, priv_key_brain=priv_key_brain, pub_key_brain=pub_key_brain, add_brain=add_brain)

@this.route("/multisig", methods=['POST', 'GET'])
def multi_sig():

    cw_1 = create_wallet()
    cw_2 = create_wallet()
    cw_3 = create_wallet()

    seed_1=cw_1[0]
    private_key_1=cw_1[1]
    public_key_1=cw_1[2]
    address_1=cw_1[3] 

    seed_2=cw_2[0]
    private_key_2=cw_2[1]
    public_key_2=cw_2[2]
    address_2=cw_2[3] 

    seed_3=cw_3[0]
    private_key_3=cw_3[1]
    public_key_3=cw_3[2]
    address_3=cw_3[3]

    return render_template('index.html', seed_1=seed_1, private_key_1=private_key_1, public_key_1=public_key_1, address_1=address_1,
                                        seed_2=seed_2, private_key_2=private_key_2, public_key_2=public_key_2, address_2=address_2,
                                        seed_3=seed_3, private_key_3=private_key_3, public_key_3=public_key_3, address_3=address_3)

@this.route("/test", methods=['POST','GET'])
def test():
    if request.method == "POST":
        todo = request.form.get("todo")
        print(todo)
    return render_template('test.html')

@this.route("/fknabt", methods=['POST', 'GET'])
def jinja():
    return render_template('PYBIT_fknabt.html')