""""
Toy RSA system:
Implement the function sign, which receives a number and a private key and returns a signature of it; and the function verify, 
which receives a number with a signature and the public key,
and returns whether the signature is valid

""""

n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def sign(m, private_key):
    return pow(m, d ,n)

def verify(m, s, public_key):
    return m == pow(s,e,n)
