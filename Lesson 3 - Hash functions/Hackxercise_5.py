"""
To see how hard it is to brute force a real hash function, try running the function you wrote in the previous exercise,
but using the full MD5. My guess is, your code will return in a few thousand years...


"""


import hashlib


def md5(s):
    return hashlib.md5(s).digest()


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
    return # same as before
