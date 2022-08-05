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


"""



def get_prg(plaintext_size, k):
        i =j = 0  
        keystream=[]
        k_list=list(k)
        print(len(k),plaintext_size)
        length=min(len(k),plaintext_size)
        for count in range(length):
             i = (i + 1) % 32
             j = (j + ord(k_list[i]))%32
             k_list[i], k_list[j]= k_list[j],k_list[i]   # swap
             Keystream_byte =str( k_list[((ord(k_list[i]) + ord(k_list[j])) %32)])
             keystream.append(Keystream_byte)
        keystream_str="".join(keystream)
        return keystream_str
"""
def fake_rc4(plaintext, keystream):
        plaintext_size=len(plaintext) 
        plaintext_list=list(plaintext)
        cipheredtext=[]
        bytes1=[]
        for count in range(len(plaintext_list)):
            print('len(plaintext_list)',plaintext_size)
            rand_key_byte=get_prg(plaintext_size, keystream,time)
            print(rand_key_byte,type(rand_key_byte))
            bytes1.append(rand_key_byte)
            if len(keystream)<=1:
                print('found it')
                break
        print('here',bytes1)
        return encrypt(plaintext,bytes1)
"""
def fake_rc4(plaintext, keystream):
    print('their shit',len(keystream))
    keystream_rc4=get_prg(len(plaintext),keystream)
    return encrypt(plaintext,keystream_rc4)

def encrypt(plaintext, k):
    ciphertxt=[chr(ord(x)^ord(y)) for x,y in zip(plaintext,k)]
    final_ciphertxt="".join((ciphertxt ))
    print('mine',final_ciphertxt)
    return (final_ciphertxt)
k=len('this is a text')
fake_rc4('12345678901234567890123456789012345678901234567890','12345678901234567890123456789012')


size=50 
plaintxt='12345678901234567890123456789012345678901234567890'
key ='12345678901234567890123456789012'
#20113369639090048556658369838361121510153189493491
