"""
In the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic captured with a sniffer (namely, Wireshark), and figure out what is the username and the password.

Submit your answers in the following text boxes. 

This hackxercise cannot be implemented on your local Python environment because the pcap file is only available inside the Codeboard system.

The traffic happens over port 8000, which scapy doesn't interpret as HTTP by default (because HTTP's default port is 80). To have it associate HTTP with port 8000, run:
bind_layers(TCP, HTTP, dport=8000)
bind_layers(TCP, HTTP, sport=8000)

There are actually two login attempts — the first one fails with "invalid credentials", and only the second one is successful.

"""
from scapy.all import *
from scapy.layers.http import *
import sys # ignore
import re 

sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_username_password():
    packets = rdpcap(recording_path)
    bind_layers(TCP, HTTP, dport=8000)
    prev_username_password = []
    for packet in packets:
        txt = packet.load.decode("utf-8")
        success = re.findall(".*Login successful!.*", txt)
        if success:
            print(prev_username_password)
        else:
            match = re.findall("username.*password=.*", txt)
            if match:
                prev_username_password = match
    pass # print Username and Password

show_username_password()
