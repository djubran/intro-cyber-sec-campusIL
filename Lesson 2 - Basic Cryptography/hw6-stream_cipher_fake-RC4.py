"""
Write the stream cipher fake-RC4: implement a function encrypt that given a plaintext and a 32-bytes key  k , returns a ciphertext encrypted with a weak variant of RC4 which we describe here.

First, implement the fake-RC4 pseudo-random generator (PRG):

It starts with  i=j=0 , and to generate the next byte in the keystream it:
Increments  i  by  1  (modulo 32),
Increments  j  by the  ith  character of the key (modulo 32),
Swaps the  ith  character of the key with its  jth  character,
Adds the  ith  character of the key and its  jth  character, modulo 32, and returns the key's character at that index.
So for example, if the  ith  character of the key was 'a' (whose ASCII value is 97), and its  jth  character was '3' (whose ASCII value is 51), their sum would be 148. Modulo the length of the key, the result will be  148%32=20 , so the pseudo random generator would return the  20th  character of the key as the next byte.

Once you have the pseudo-random generator working, the rest is easy:

Iterate over the plaintext
XOR every character with the next byte of the pseudo-random generator's keystream
Return the result as the ciphertext!

p.s. passed all tests
"""



def get_prg(plaintext_size, k):
        i=0 
        j = 0  
        keystream=""
        k_list=list(k)
        for count in range(plaintext_size):
             i = (i + 1) % 32
             j = (j + ord(k_list[i]))%32
             k_list[i], k_list[j]= k_list[j],k_list[i]   # swap
             keystream += k_list[((ord(k_list[i]) + ord(k_list[j])) %32)]
        return keystream
    
        
def fake_rc4(plaintext, keystream):
    return encrypt(plaintext,keystream)


def encrypt(plaintext, k):
    ciphertxt=[chr(ord(x)^ord(y)) for x,y in zip(plaintext,k)]
    final_ciphertxt="".join((ciphertxt ))
    return final_ciphertxt
