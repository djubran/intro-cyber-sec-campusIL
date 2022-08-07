"""
hw2- Implement Caesar’s cipher: implement a function encrypt that given a plaintext string and a key k (how many letters to shift), 
returns a ciphertext where each character is shifted k places.
You can assume all characters are lowercase letters, with no punctuation or spaces backward (so with k=2 'c' is encrypted by 'a')
"""


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    encryptedtext = []
    for letter in plaintext:
        i = alphabet.index(letter)
        j = (i - k) % len(alphabet)
        encryptedtext.append(alphabet[j])
    return ''.join(encryptedtext)
