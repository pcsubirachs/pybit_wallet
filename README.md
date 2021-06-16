# PyBit

### An open-source python flask app to generate simple, multi-sig, and brain phrase Bitcoin wallets

### Home Page

<img src="https://github.com/pcsubirachs/pybit_wallet/blob/main/media/home_page.jpeg " alt="drawing" align="middle" width="800"/>

### Creating a simple Bitcoin wallet

<img src="https://github.com/pcsubirachs/pybit_wallet/blob/main/media/simple.jpeg" alt="drawing" align="middle" width="800"/>

### Create a 2 of 3 multi-sig wallet

<img src="https://github.com/pcsubirachs/pybit_wallet/blob/main/media/K_of_N.jpeg" alt="drawing" align="middle" width="800"/>

### Create a brain phrase wallet

<img src="https://github.com/pcsubirachs/pybit_wallet/blob/main/media/brain_phrase.jpeg" alt="drawing" align="middle" width="800"/>

## Link to App
[PyBit: An open-source Bitcoin wallet generator](https://github.com/pcsubirachs/pybit_wallet "PyBit")

## How it Works

Use this app to generate simple original, multi-sig or brain phrase Bitcoin wallets. *WARNING* DO NOT USE THESE WALLETS TO SEND MONEY TO. This app is experimental ONLY.

### Simple Wallet

The simple wallet generates a bitcoin wallet with a seed phrase, private key, public key, and a bitcoin 
wallet address. A seed phrase allows you to backup your Bitcoin from anywhere. 
A private key is derived from your seed. A public key is derived from your private
key using a SHA256 one-way cryptographic algorithm. A bitcoin wallet is a compressed
form of your public key.

### Multi-Sig Wallet

A 2 of 3 multi signature wallet allows the user to create 3 addresses, where 2 are needed for spending a transaction.

## Brain Phrase

A brain phrase wallet allows you to use phrase memorization to create a wallet and cross borders with billions in your head. Install and run this app locally to recover your funds.

# Developer: Setup & Install

1. Ensure Python3 is downloaded on your machine

2. Fork the repo, navigate to local folder in terminal

3. Install pipenv on your computer using pip. Only need to run this command once for initial install.

<code>pip install pipenv</code>

4. Boot into your local pipenv virtual environment.

<code>pipenv shell</code>

5. Install the packages in the Pipfile to your virtual environment.

<code>pipenv install</code>

6. Pointer to Flask App

<code>export FLASK_APP=web_app</code>

7. Debug code more easily in developer mode.

<code>export FLASK_ENV=developer</code>

8. Now run the application on your local server.

<code>flask run</code>

#### Final 

<bold>Should now be running on http://127.0.0.1:5000/</bold>


