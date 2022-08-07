"""
hw3-Below is code that implements an InvertedCaesar cipher: its encryption shifts letters k places forward.

Find the plaintext and key of the following message that was encrypted using InvertedCaesar

kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe . . . answer:- message : thecavalrywillattackfromthenorthwestatnoon , key=17
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    for k in range(26):
        plaintext = []
        for c in ciphertext:
            i = alphabet.index(c)
            j = (i - k) % len(alphabet)
            plaintext.append(alphabet[j])
        print( ''.join(plaintext),k)  
    
     #print all (plaintext, k) possibilities and copy the right one to the Edx platform
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
