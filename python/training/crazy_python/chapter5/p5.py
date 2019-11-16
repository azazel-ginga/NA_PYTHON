#coding=utf-8
'''
lambda表达式语法格式:
	lambda [parameter_list]:表达式
	lambda语法格式的特点如下：
	1.lambda表达式必须使用lambda关键字定义
	2.在lambda之后、冒号左边是参数列表，右边是表达式返回的值
	举例:
	lambda x,y:x+y
	可以改写为
	def add(x,y):
		return x + y
'''


#传入计算平方的lambda表达式作为参数:
t = map(lambda x:x * x,range(8))
result = [e for e in t]
print(result)

y = map(lambda x:x * x if x % 2 ==0 else 0,range(8))  #当平方为偶数时输出，不为偶数时输出0
result = [e for e in y]
print(result)