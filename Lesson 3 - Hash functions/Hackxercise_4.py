"""
The function weak_md5 is a "weaker" version of MD5, using only the first 5 bytes of the MD5 hash. This means its hashing size is
n=40  and it can be brute forced rather easily.

Implement a function find_collisions that loops over all the possible strings until it finds an arbitrary collision - that is, 
two different strings whose hash is the same - and returns them (as a tuple).



"""

import hashlib
import itertools

def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    ascii_str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    dic = {}
    #create permutations of varying lengths
       #check every permutation at fixed length for a match  
    
    for r in range(40):
        for elem in itertools.product(ascii_str, repeat=r):
            permutation = ''.join(elem)
            md5 = weak_md5(permutation)
            #check if hash code already in dictionary
            if md5 in dic:
                return permutation, dic[md5]
            # hash code s new add to dic
            dic[md5] = permutation 
            
    return # return (s1, s2) such that s1 != s2 and weak_md5(s1) == weak_md5(s2)
