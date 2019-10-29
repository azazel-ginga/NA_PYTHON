#99乘法表

def multipletable():
	for i in range(1,10):
		for j in range(1,i+1):
			print(i ,"*", j,"=" , (i * j)," ",end = "")          #end = ""   用于讲字符串在同行输出
		print("\r")

multipletable()
