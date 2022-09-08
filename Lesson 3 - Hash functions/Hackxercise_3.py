""""

Brute-force the hash function you've just written!

Implement a function crack that given a string s, loops until it finds a different string that collides with it, and returns the different string.

It's pretty tricky to implement a loop over all the possible strings of a certain length... unless you know the Python standard library well enough! 
Check out itertools.product and use it to your advantage


""""
import string
from itertools import permutations

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    ascii_str = string.printable
    hashed = simple_hash(s)
    #create permutations of varying lengths
    for r in range(len(ascii_str)+1): 
       #check every permutation at fixed length for a match  
        for perm in list(permutations(ascii_str,r)):
            if s != ''.join(perm) and simple_hash(s) == simple_hash(''.join(perm)) :
                return ''.join(perm) #match found return the permuation that provides it
        


