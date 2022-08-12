"""
Use PyCrypto to encrypt and decrypt with AES-CBC:

Implement a function encrypt, that given a plaintext and a  16 -byte ( 128  bit) key  k , picks a random  16 -byte ( 128  bit) IV, and returns a ciphertext encrypted with AES-CBC with the IV prepended to the ciphertext (in bytes).

You may assume that the plaintext length (in bytes) is a multiple of 16.

Implement a function decrypt, that given a ciphertext (as formatted by the encrypt function) and a  16 -byte ( 128  bit) key  k , returns the plaintext as decrypted by AES-CBC (in 'latin1').

"""

from Crypto.Cipher import AES
from Crypto import Random


def aes_encrypt(plaintext, key):
    # generate IV
    IV = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC,IV)
    ciphertxt=IV+cipher.encrypt(plaintext)
    return ciphertxt # return iv + ciphertext (in bytes)

def aes_decrypt(ciphertext, k):
    IV_C0 = ciphertext[:AES.block_size]
    cipher = AES.new(k, AES.MODE_CBC, IV_C0)
    plaintext=cipher.decrypt(ciphertext[AES.block_size:])#start decrypting from C1 onwards
    return plaintext.decode('latin1') # return plaintext (in 'latin1')
