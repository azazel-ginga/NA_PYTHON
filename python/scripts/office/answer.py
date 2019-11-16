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


a = 1
b = 2
c = 2
d = 3
e = 4
while a < doc.Paragraphs.count:
	para = doc.Paragraphs[a]
	line1 = para.Range.text
	para = doc.Paragraphs[c]
	line2 = para.Range.text
	para = doc.Paragraphs[d]
	line3 = para.Range.text
	para = doc.Paragraphs[e]
	line4 = para.Range.text
	sheet1.Cells(b,9).value = line1
	sheet1.Cells(b,10).value = line2
	sheet1.Cells(b,11).value = line3
	sheet1.Cells(b,12).value = line4
	b += 1
	a += 7
	c += 7 
	d += 7
	e += 7 




excel.Save()	
excel.Close()
doc.Close()