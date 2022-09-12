""""
A toy RSA system:
Implement the function encrypt, which receives a number and a public key and returns the encrypted number; 
and the function decrypt, which receives an encrypted number and the private key, and returns the original number.

Python has a built-in modular exponentiation function.

""""

n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def encrypt(m, public_key):
    return pow(m,e,n)

def decrypt(c, private_key):
    return pow(c,d,n)
