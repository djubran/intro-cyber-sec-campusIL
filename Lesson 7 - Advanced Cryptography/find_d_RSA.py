"""
With  p=7  and  q=5  and  e=11 , what would be an appropriate  d  (given that  d<25 )?
"""
#RSA paramaters
p = 7
q = 5
n = p*q
e = 11
phi = (p-1)*(q-1)

for d in range(25):
    if ((d*e) % phi) == 1: 
        print(d)
        break
