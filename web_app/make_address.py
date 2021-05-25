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
