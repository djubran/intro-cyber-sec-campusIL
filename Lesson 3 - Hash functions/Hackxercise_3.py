""""

Brute-force the hash function you've just written!

Implement a function crack that given a string s, loops until it finds a different string that collides with it, and returns the different string.

It's pretty tricky to implement a loop over all the possible strings of a certain length... unless you know the Python standard library well enough! 
Check out itertools.product and use it to your advantage


""""
import itertools
import string 

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    ascii_str = string.printable
    hashed_s = simple_hash(s)
    r = 1
    #create permutations of varying lengths
    while True : 
       #check every permutation at fixed length for a match  
        all_permutations = list(itertools.product(ascii_str, repeat=r))
        for permutation in all_permutations:
            if s != ''.join(permutation) and simple_hash(s) == simple_hash(''.join(permutation)) :
                return ''.join(permutation) #match found return the permuation that provides it
        r += 1
    return # return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)
