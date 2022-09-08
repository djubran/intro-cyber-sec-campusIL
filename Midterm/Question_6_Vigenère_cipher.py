"""
uestion 6
12.5 points

The Vigenère cipher is a method of encryption using a series of interwoven Caesar ciphers.

It takes a codeword for a key – for example, "LEMON". Then, given a plaintext, such as "ATTACKATDAWN", it repeats the codeword until it matches the length of the plaintext:

L	E	M	O	N	L	E	M	O	N	L	E
A	T	T	A	C	K	A	T	D	A	W	N
Finally, it encrypts every letter using a Caesar cipher shifted to the corresponding letter of the codeword. So, for example:

The first "A" is encrypted using a Caesar cipher of A → L (+11), so it becomes L.
The first "T" is encrypted using a Caesar cipher of A → E (+4), so it becomes X.
The second "T" is encrypted using a Caesar cipher of A → M (+12), so it becomes F.
Subsequently, we get:
LXFOPVEFRNHR

Implement a function, vigener_encrypt(plaintext, codeword), which takes a plaintext and codeword (both in 


"""


# plaintext and codeword in CAPITAL LETTERS  only
alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
def ceaser_encrypt(plaintext, k):
    encryptedtext = []
    alphabet = alphabet_lowercase.upper()
    for letter in plaintext:
        i = alphabet.index(letter)
        j = (i + k) % len(alphabet)
        encryptedtext.append(alphabet[j])
    return ''.join(encryptedtext)
    
def vigenere_encrypt(plaintext, codeword):
    vigenere_enc_txt = ''
    if len(plaintext) == len(codeword): 
        codeword = list(codeword) 
    elif len(plaintext) < len(codeword):
        codeword = codeword[:len(plaintext)-1]
        print('shortened cofdeword is' ,codeword)
    else: 
        codeword = list(codeword) 
        for i in range(len(plaintext) -len(codeword)): 
          codeword.append(codeword[i % len(codeword)])
          print('codeword repharsed is ',codeword)
    for elem in range( len(codeword)):
        print('A->' ,codeword[elem],' ',ord(codeword[elem])-ord('A'), 'convert this ',plaintext[elem] , 'ietration no. ',elem)
        vigenere_enc_txt += ceaser_encrypt(plaintext[elem] ,ord(codeword[elem])-ord('A'))
        print(vigenere_enc_txt)
    print(len(plaintext),len(codeword),len(vigenere_enc_txt))
    return vigenere_enc_txt
    
vigenere_encrypt('ASDFGHJK ','QWERTYUI')
vigenere_encrypt('ATTACKATDAWN ','LEMON')
vigenere_encrypt('YO ','KITCH')
