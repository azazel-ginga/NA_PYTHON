from scapy.all import *

dip = "173.63.1.2"
payload = "A"*496+"B"*500
packet = IP(dst=dip)/UDP(sport=1500,dport=1501)/payload
 
frags = fragment(packet,fragsize=500)
 
counter = 1
for fragment in frags:
  print ("Packet no#"+str(counter))
  print ("===================================================")
  fragment.show() #displays each fragment
  counter += 1
  send(fragment)