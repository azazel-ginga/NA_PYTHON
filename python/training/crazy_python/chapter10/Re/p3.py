#coding = utf - 8

'''
re.findall(pattern,string,flags=0):扫描整个字符串，并返回字符串中所有匹配pattern的子串
组成的列表。其中pattern参数代表正则表达式:string代表被匹配的字符串;flags则代表正则表达式的匹配
旗标。


re.finditer(pattern,string,flags=0):扫描这个字符串，并返回字符串中所有匹配的pattern的子串
组成的迭代器，迭代器的元素是_sre.SRE_Match对象。其中pattern参数代表正则表达式;string代表被匹配
的字符串;flags则代表正则表达式匹配旗标。



总结:findall()函数返回所有匹配pattern的子串组成的列表;而finiter()函数则返回所有匹配pattern的子串
组成的迭代器.


正则表达式旗标

re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

'''

import re

#返回所有匹配pattern的子串组成的列表，忽略大小写
print(re.findall('fkit','Fkit is very good,Fkit.org is my favorite',re.I))

#返回所有匹配pattern的子串组成的迭代器，忽略大小写
it = re.finditer('fkit','Fkit is very good,Fkit.org is my favorite',re.I)
for e in it:
	print(str(e.span()) + "-->" + e.group())