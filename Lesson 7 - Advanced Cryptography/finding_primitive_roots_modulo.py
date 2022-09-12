"""
What would be good bases for the prime 13?

"""
# import random module
import random


def find_bases(p,repeats):
 bases = []
 while   repeats:
    remainder = []
    g = random.randint(1, p-1)
    a = random.randint(1, p-1)
    
    for a in range(p):
        r = pow(g, a, p)
        if (r <= p-1) and (r not in remainder) :
            remainder.append(r)
            
    if len(remainder) == p-1:
        bases.append(g)
        
    repeats = repeats -1
 print(list(set(bases)))
    
find_bases(13,200)
