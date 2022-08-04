"""
hw4- xor, one time pad 
Eve managed to intercept the following ciphertext, created using a one-time-pad: '\x56\x10\x34\xf8'. She tried to brute-force it, and got the following possible plaintexts:

ball (if the random keystream was '\x34\x71\x58\x94')
cake (if the random keystream was '\x35\x71\x5f\x9d')
poem (if the random keystream was '\x26\x7f\x51\x95')
What is the most plausible plaintext?

answer: There's no way to know - any 4-letter word is just as plausible
Eve managed to intercept another ciphertext: '\x46\x06\x3e\xf3'. She suspects it was encrypted using the same random keystream as the last intercepted message, thus compromising the perfect security of the one-time-pad.

If she is correct, what would be the most plausible plaintext of the first message?

ball
cake
poem

answer: cake  , used code below
"""

msg1="\x56\x10\x34\xf8" #first logical message cracked
msg2='\x46\x06\x3e\xf3' #second logical message cracked

x='\x35\x71\x5f\x9d' #first suspected key
y='\x34\x71\x58\x94' #second suspected key
z='\x26\x7f\x51\x95' #third suspected key

#checking which key is the right one ou of the three by brute forcing

#first key
word_x_1 = [chr((ord(a) ^ ord(b))) for a,b in zip(msg1, x)]
print(word_x_1)
word_x_2 = [chr((ord(a) ^ ord(b))) for a,b in zip(msg2, x)]
print(word_x_2)

#second key
word_y_1 = [chr((ord(a) ^ ord(b))) for a,b in zip(msg1, y)]
print(word_y_1)
word_y_2 = [chr((ord(a) ^ ord(b))) for a,b in zip(msg2, y)]
print(word_y_2)

#third key
word_z_1 = [chr((ord(a) ^ ord(b))) for a,b in zip(msg1, z)]
print(word_z_1)
word_z_2 = [chr((ord(a) ^ ord(b))) for a,b in zip(msg2, z)]
print(word_z_2)
