
"""
Brute force a message encrypted with AES-CBC, given that it was encrypted with a key that represents a phone number of someone from Tel-Aviv, padded with zeroes (in other words, 9 digits, beginning with 036, and with trailing '0' to a length of 16 bytes, like this: 036######0000000).

You should test your brute-force cracker code using the outputs from your encrypt function of Hackxercise 6.


"""

from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

def brute_force_aes(ciphertext):
    for i in range(999999):
        key_t = ('036' + str(i).zfill(6) + '0000000')
        key=key_t.encode()
        plaintext=aes_decrypt(ciphertext,key)
        print(plaintext)
        if is_english(plaintext):
            return (plaintext , key)
    
