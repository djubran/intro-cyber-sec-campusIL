"""
Real RSA system:
Use pycrypto to sign and verify a message using RSA.


"""


from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def sign(m, private_key):
    privKey = RSA.importKey(private_key)
    return pow(m, privKey.d, privKey.n)

def verify(m, s, public_key):
    pubKey = RSA.importKey(public_key)
    return m == pow(s, pubKey.e, pubKey.n)
