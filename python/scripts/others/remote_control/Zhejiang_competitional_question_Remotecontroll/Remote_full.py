import os
import paramkip
import threading
# flag1=F1_F2_F3

def ssh2(ip,username,passwd,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# flag2=F4_F5_F6;

		ssh.Connect(ip,username,passwd,timeout=5)
		stdin,stdout,stderr = ssh.exec_command(cmd)
		stdin.write("Y")
# flag3=F7_F8_F9
		
		out=stdout.read()
		file=open("result.txt","a")
		file.write(out)
		file.write(ip)
		file.close()
	except:
		print ("target connect faild! %s" %ip)

if __name__ == '__main__':
	targets_cmd = "cat /etc/passwd|grep /bin/bash"
	targets_user = "root"
	targets_pass = "123456"
	#F15

	threads = []
	for i in range(10):
		targets_ip = "192.168.1."+str(i)
		a=threading.Thread(target=ssh2,args=(targets_ip,targets_user,targets_pass,targets_cmd))
		a.start()
# flag5=F11_F12_F13_F14_F15_F16_F17_F18
