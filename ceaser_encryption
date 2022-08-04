alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    encryptedtext = []
    for letter in plaintext:
        i = alphabet.index(letter)
        j = (i - k) % len(alphabet)
        encryptedtext.append(alphabet[j])
    return ''.join(encryptedtext)
