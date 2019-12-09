#coding = utf - 8

import re

'''
子表达式:
正则表达式还支持圆括号表达式，用于将多个表达式组成一个子表达式，在圆括号中可以使用或运算符(|)


子表达式(组)支持如下用法:
(exp):匹配exp表达式并捕获成一个自动命名的组，后面可以通过"\1"以用第一个捕获组
所匹配的子串，通过"\2"引用第二个捕获组所匹配的子串……依此类推


'''
#示例代码如下:
print(re.search(r'Windows (95|98|NT|2000)[\w ]+\1','Windows 98 published in 98'))
#输出:<_sre.SRE_Match object; span=(0, 26), match='Windows 98 published in 98'>


'''
在上面代码中用到的正则表达式是r'Windows (95|98|NT|2000)[\w ]+\1',其中(95|98|NT|2000)是一个组
该组可匹配95、98、NT、2000;接下来是[\w ](也可以写成[\w|\s])，这个括号表达式可以匹配任意单词字符和空格
方括号后面的"+"表示方括号表达式可出现1~N次;最后是"\1",引用第一个组所匹配的子串————假如第一个组匹配98，那么
"\1"也必须是98，因此该正则表达式可匹配"Windows 98 published in 98"
'''

#将到代码改成如下形式:
print(re.search(r'Windows (95|98|NT|2000)[\w ]+\1','Windows 98 published in 95'))
#输出:None

'''
上面代码中第一个组匹配的子串是98,因此"\1"应该引用子串98，所以该正则表达式无法匹配"Windows 98 published in 95"

'''
