"""

In the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic captured with a sniffer (namely, Wireshark),
and figure out what is the destination port of the third packet, and the source port address in the fourth packet.

Submit your answers in the following text boxes. 

This hackxercise cannot be implemented on your local Python environment because the pcap file is only available inside the Codeboard system.



"""
from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

def show_source_destination_ports():
    packets = rdpcap(recording_path)
    print(packets[2][TCP].dport,packets[3][TCP].sport)
    pass # print destination port of third packet and source port of fourth packet

show_source_destination_ports()

