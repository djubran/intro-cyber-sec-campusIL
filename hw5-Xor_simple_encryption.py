"""
Write a XOR cipher: implement a function encrypt that given a plaintext string and a key  k  
(also a string), returns a ciphertext where each character is XORed with its respective character in  k .
Assume that the plaintext and key have the same length. (that is, plaintext[i] is XORed with k[i]).

"""

def encrypt(plaintext, k):
    ciphertxt=[chr(ord(x)^ord(y)) for x,y in zip(plaintext,k)]
    final_ciphertxt="".join((ciphertxt ))
    return (final_ciphertxt)
    
    
encrypt('1100', '1110')
