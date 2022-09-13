""""
Implement the function weak-HMAC, which receives message and a  8 -bytes ( 64 -bit) long key, 
and returns its HMAC using SHA-1 with the given  8 -byte ( 64 -bit) ipad and opad.

"""
from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'

def weak_hmac(m, k, ipad, opad):
    #xored key with bit patterns
    Sipad = [a ^ b for a, b in zip(k, ipad)]
    Sopad = [a ^ b for a, b in zip(k, opad)]
    
    #inner activation
    hash_inner = sha1()
    hash_inner.update(bytes(Sipad))
    hash_inner.update(m)
    
    #outer activation
    hash_outer = sha1()
    hash_outer.update(bytes(Sopad))
    
    #inpur inner hashing result to outer hash
    hash_outer.update(hash_inner.digest())
    return hash_outer.hexdigest()    
