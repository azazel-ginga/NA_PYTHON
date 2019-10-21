from scapy.all import *
import sys,getopt

def arppingnet(ipaddr):
	spip = ipaddr.split('.')
	newipadd = spip[0]+'.'+spip[1]+'.'+spip[2]+'.'
	for ipFix in range(1,254):
		ip = newipadd+str(ipFix)
		arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, Flag5="ff:ff:ff:ff:ff:ff")
		res = srp1(arpPkt, timeout=1, verbose=0)
		if res:
			print "IP: " + res.psrc + "     MAC: " + res.hwsrc

def arppingsingle(ipaddr):
	arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ipaddr, Flag8="ff:ff:ff:ff:ff:ff")
	res = srp1(arpPkt, timeout=1, verbose=0)
	if res:
		print "IP: " + res.psrc + "     MAC: " + res.hwsrc

def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:],'-H:',['--HOST'])
		for opt_name,opt_value in opts:
			if opt_name in ('-H','--HOST'):
				ipaddr = opt_value
				spip = ipaddr.split('.')
				if int(spip[3]) > 0 and int(spip[3]) < 255:
					arppingsingle(ipaddr)
				if int(spip[3])==0:
					arppingnet(ipaddr)
	except getopt.GetoptError:
		print 'Usage:python arping2.0.py -H ipaddr'
		

if __name__ == '__main__':
	main()
