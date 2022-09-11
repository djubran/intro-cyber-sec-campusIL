""""

In an imaginary protocol stack, the header structures are as follows:

Layer 1 has the following structure:
The first  4  bytes are the ID of the sender
The next  4  bytes are the ID of the receiver
The next  4  bytes are the size of the content (let's call it  n )
The next  n  bytes are the content
Layer 2 has the following header and footer:
The first  4  bytes are the session ID
The last  4  bytes are a checksum of the message
The middle bytes are the content
Layer 3 has the following structure:
The first  4  bytes are the message ID
The rest of the bytes are the message
here is a message captured on the wire, that was sent using this protocol stack.

b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

Write a Python program to decode the captured message and print out the contents of the following fields:
sender ID, message ID, message text, and the checksum.

Note that all the IDs and numbers in the message are unsigned  4 -byte integers, encoded in little endian format.
You need to print and submit them as normal (decimal) numbers.


""""
from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

#### Don't change the code until this line ####

def show_details():
    sender_ID, receiver_ID, content_size, session_ID, message_ID = unpack("<IIIII", packet[:20])
    message_txt = packet[20:-4].decode('UTF-8')
    checksum = unpack("<I", packet[-4:])
    print("Sender ID:",sender_ID," message ID:",message_ID," Message: ",message_txt," checksum:",checksum )



    pass # print sender ID (decimal), message ID (decimal), the actual message (readable english text), and its checksum (decimal)

show_details()
