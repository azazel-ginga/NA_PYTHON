#coding = utf - 8 



import threading
import time
import sys


con = threading.Condition()
num = 0
index = 0


class Th1(threading.Thread):
	def __init__(self):
		super().__init__()
	
	def run(self):
		global num
		global index
		con.acquire()
		while True:
			num += 1
			index += 1
			print("当前线程为:" + threading.current_thread().name + "_" + str(num))
			if index >= 5:
				index = 0
				con.notify()
				#con.wait()
				con.release()
				if num < 15:
					pass
				else:
					con.release()
					sys.exit(0)
		con.release()


class Th2(threading.Thread):
	def __init__(self):
		super().__init__()
	
	def run(self):
		global num
		global index
		con.acquire()
		while True:
			num += 1
			index += 1
			print("当前线程为:" + threading.current_thread().name + "_" + str(num))
			if index >= 5:
				index = 0
				con.notify()
				#con.wait()
				con.release()
				if num < 15:
					pass
				else:
					con.release()
					sys.exit(0)
		con.release()


class Th3(threading.Thread):
	def __init__(self):
		super().__init__()
	
	def run(self):
		global num
		global index
		con.acquire()
		while True:
			num += 1
			index += 1
			print("当前线程为:" + threading.current_thread().name + "_" + str(num))
			if index >= 5:
				index = 0
				con.notify()
				#con.wait()
				con.release()
				if num < 15:
					pass
				else:
					con.release()
					sys.exit(0)
		con.release()


t1 = Th1()
t1.start()
t1.join()
t2 = Th2()
t2.start()
t2.join()
t3 = Th3()
t3.start()
t3.join()

print(num)


			
		












