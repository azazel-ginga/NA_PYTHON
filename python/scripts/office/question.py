#coding:utf-8
import docx	
import xlrd
import win32com
import re

from win32com.client import Dispatch,DispatchEx
word = Dispatch('Word.Application')
xl = Dispatch('Excel.Application')
#word.Visible = 0              //Do not open the application
#word.DisplayAlerts = 0        //Do not Alert

doc = word.Documents.Open(FileName='D:\\file\\1.docx',Encoding='gbk')
excel = xl.Workbooks.Open('D:\\file\\ex.xls')

sheet1 = excel.Worksheets('作业库')
print(doc.Paragraphs.count)


a = 0
b = 2
while a < doc.Paragraphs.count:
	para = doc.Paragraphs[a]
	line = para.Range.text
	sheet1.Cells(b,3).value = line
	b += 1
	a += 7




excel.Save()	
excel.Close()
doc.Close()