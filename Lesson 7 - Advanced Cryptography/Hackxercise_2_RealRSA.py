"""
A real RSA system:
Use pycrypto to encrypt and decrypt a message using RSA.

"""
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    pubKeyObj =  RSA.importKey(public_key)
    return pow(m, pubKeyObj.e, pubKeyObj.n) # return ciphertext and key

def decrypt(c, private_key):
    privKeyObj = RSA.importKey(private_key)
    return pow(c, privKeyObj.d, privKeyObj.n)
