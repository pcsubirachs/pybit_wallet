# create_btc_wallet.py

from pywallet import wallet


def create_wallet():
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()

    # create bitcoin wallet in JSON format
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)

    coin = w['coin']
    seed = w['seed']
    priv_key = w['xprivate_key']
    pub_key = w['xpublic_key']
    address = w['address']
    wif = w['wif']

    # children, derived from priv key
    child_path = w['children'][0]['path']
    child_bip32_path = w['children'][0]['bip32_path']
    child_pub_key = w['children'][0]['xpublic_key']
    child_address = w['children'][0]['address']
    #child_pub_key_prime = w['children'][0]['xpublic_key_prime']

    arr = [seed, priv_key, pub_key, address]

    return arr

# Testing

#print(w)
#print("Seed Phrase: ", seed)
#print("Private Key: ", priv_key)
#print("Public Key: ", pub_key)
#print("Address: ", address)

cw = create_wallet()
print(cw[0])