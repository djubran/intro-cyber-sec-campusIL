"""
Use PyCryptoDome to build the real version of the last hackxercise: implement a function encrypt that given a plaintext and a 32-bytes key  k
, returns a ciphertext encrypted with the actual RC4 cipher.

"""

from Crypto.Cipher import ARC4

def rc4(plaintext, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext)
