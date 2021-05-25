from bitcoin import *

"""
----- REFERENCE -----
# generate private key
private_key = random_key()
print("Private Key: ", private_key)

# convert private key to public key
public_key = privtopub(private_key)
print("Public Key: ", public_key)

# then, create a readable Bitcoin address
address = pubtoaddr(public_key)
print("Super fresh Bitcoin Address: ", address)

# brain wallet
priv_key_brain = sha256('I love Yami')
pub_key_brain = privtopub(priv_key_brain)
add_brain = pubtoaddr(pub_key_brain)
print("Brain Bitcoin Address: ", add_brain)

# get history of a wallet
#history = history(bc1q7tqwjga443h9glcjv6fu79nsd8ye5etcc3zrxh)
#print("History: ", history)

# multisig
print("* * * * * * * * * * * ----- MULTI-SIG ----- * * * * * * * * * * * ")
priv1 = random_key()
print("Private Key 1: ", priv1)
pub1 = privtopub(priv1)
priv2 = random_key()
print("Private Key 2: ", priv2)
pub2 = privtopub(priv2)
priv3 = random_key()
print("Private Key 3: ", priv3)
pub3 = privtopub(priv3)


# gives us a multi sig script
multi_sig = mk_multisig_script(pub1, pub2, pub3, 2, 3)
#print("Multi :", multi_sig)

# need to convert script to hash, P2SH or Pay-to-Script Hash
multi_addr = scriptaddr(multi_sig)
print("Multi Sig Address :", multi_addr)


# Pybit

## An open-source python Flask app to generate simple, multi-sig, and brain phrase Bitcoin wallets

### Home Page

<img src="https://github.com/pcsubirachs/pybit_wallet/media/home_page.jpeg " alt="drawing" align="middle" width="800"/>

### Creating a simple Bitcoin wallet

<img src="https://github.com/pcsubirachs/pybit_wallet/media/simple.jpeg" alt="drawing" align="middle" width="800"/>

### Create a K of N multi-sig wallet

<img src="https://github.com/pcsubirachs/pybit_wallet/media/K_of_N.jpeg" alt="drawing" align="middle" width="800"/>

### Create a brain phrase wallet

<img src="https://github.com/pcsubirachs/pybit_wallet/media/brain_phrase.jpeg" alt="drawing" align="middle" width="800"/>

## Link to App
[PyBit: An open-source Bitcoin wallet generator](https://github.com/pcsubirachs/pybit_wallet "PyBit")

## How it Works

Use this app to generate simple original, multi-sig or brain phrase Bitcoin wallets.

### Simple Wallet

Description here...

### Multi-Sig Wallet

Description here...

## Brain Phrase

Description here....

# Developer: Setup & Install

1. Fork repo

2. pip install pipenv

3. pipenv shell

4. pipenv install pip

5. export FLASK_APP=web_app

6. export FLASK_ENV=developer

7. flask run

Should now be running on http://127.0.0.1:5000/

"""

def make_address():
    # generate private key
    private_key = random_key()
    # convert private key to public key
    public_key = privtopub(private_key)
    # then, create a readable Bitcoin address
    address = pubtoaddr(public_key)
    
    return address

def bp(phrase):
    # generate private key from input
    bp.priv_key_brain = sha256(phrase)
    # generate public key from your private key
    bp.pub_key_brain = privtopub(priv_key_brain)
    # then create a readable Bitcoin address
    bp.add_brain = pubtoaddr(pub_key_brain)

    return bp.add_brain, bp.priv_key_brain, bp.pub_key_brain
