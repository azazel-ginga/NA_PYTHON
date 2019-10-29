#打印多行分隔符

#def sperating(mark,times):
#	print(str(mark) * times)


def sperating(mark,times,rows):
	a = 0
	while(a < rows):
		print(str(mark) * times)
		a+=1


mark = "("
times = 50
lines = 3
sperating(mark,times,lines)