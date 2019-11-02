#coding=utf-8

'''
将一个浮点数转换成人名币读法的字符串。实现这个函数的思路是，首先吧这个浮点数分成整数部分和小数部分。提取整数部分（直接将浮点数强转成整数即可）
再使用浮点数减去整数就可以得到这个浮点数的小数部分。

小数部分处理：直接保留两位数字，转换成几角几分

整数部分处理：以中国数字记数的习惯，4位一节，一个4位的数字可被转成几千几百几十几，如果这节4位数字出现在1-4位，则后面添加单位“元”，如果这节数字
出现在5-8位，则后面添加单位“万”，如果这节数字出现在9-12位，则后面添加单位“亿”；多余十二位就暂不考虑了。

程序的关键就是把一个4位的数字字符串转换成中文读法。


'''
import decimal


class Numtormb(object):

	def __init__(self,num):
		self.num = num
		self.integer = 0
		self.float = 0

	def __divide(self):
		self.integer = int(self.num)
		self.float = self.num - self.integer



	def __handlenum(self):
		self.__divide()

		#handling the decimals part
		strfloat = str(self.float)
		if len(str(strfloat)) > 4:
			self.float = round(self.float,2)
			strfloat = str(self.float)
			strfloat = strfloat[2] + '角' + strfloat[3] + '分'
		elif len(str(strfloat)) == 1:
			strfloat = '0角' + '0分'
		elif len(str(strfloat)) == 3:
			strfloat = str(self.float)
			strfloat = strfloat[2] + '角' + '0分' 

		#handling the integer part
		strinteger = str(self.integer)
		if len(strinteger) >= 0 and len(strinteger) <= 4:
			strinteger = strinteger + '元'
		elif len(strinteger) > 4 and len(strinteger) <=8:
			strinteger = strinteger + '万'
		elif len(strinteger) > 5 and len(strinteger) <=12:
			strinteger = strinteger + '亿'

		return strinteger + strfloat

	def outputform(self):
		print(self.__handlenum())


n1 = Numtormb(111111111111.01)
n1.outputform()


